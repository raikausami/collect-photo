@echo off

for /f %%a in (filename_list.txt) do (
 python trimming_angle.py neruf %%a
 
)