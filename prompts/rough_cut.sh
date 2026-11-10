#!/bin/bash
set -e
A=/home/claude/treg-ugc-assets/audio
V="scale=854:480,fps=24,setsar=1"
ffmpeg -v error -y -ss 2.0 -t 0.5 -i c1_S1.mp4 -an -vf "$V" s1.mp4
ffmpeg -v error -y -t 1.9 -i c2_S2.mp4 -an -vf "$V" s2.mp4
ffmpeg -v error -y -t 2.4 -i c3_S3a.mp4 -an -vf "$V" s3.mp4
ffmpeg -v error -y -t 5.0 -i ${C4:-c4_S3b.mp4} -an -vf "$V" s4.mp4
ffmpeg -v error -y -i c5_S4.mp4 -an -filter_complex "[0:v]trim=0:2.0,setpts=PTS-STARTPTS,$V[a];[0:v]trim=2.0,setpts=(PTS-STARTPTS)/2,$V[b];[a][b]concat=n=2:v=1[v]" -map "[v]" s5.mp4
printf "file s1.mp4\nfile s2.mp4\nfile s3.mp4\nfile s4.mp4\nfile s5.mp4\n" > list.txt
ffmpeg -v error -y -f concat -safe 0 -i list.txt -c copy v.mp4
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 v.mp4)
ffmpeg -v error -y -i v.mp4 -i $A/vo_leader_still-paying.mp3 -i $A/vo_hero_3x-cheaper.mp3 -i $A/vo_hero_price.mp3 -i $A/vo_leader_told-you.mp3 -filter_complex "[1]adelay=500|500[a1];[2]adelay=2400|2400[a2];[3]adelay=4800|4800[a3];[4]adelay=9800|9800[a4];[a1][a2][a3][a4]amix=inputs=4:normalize=0,apad[a]" -map 0:v -map "[a]" -t $D -c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 192k hook_480p_draft.mp4
echo $D
