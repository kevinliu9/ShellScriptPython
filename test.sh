cd /mnt/c/Users/Kevin\ Liu/Desktop/osu!\ mp3s
for file in *; do
   if [ ${file: -4} == ".mp3" ]
   then
      echo "$(ffprobe -v error -select_streams a:0 -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1 "$file") | $(ffprobe -loglevel error -show_entries format_tags=title -of default=noprint_wrappers=1:nokey=1 "$file") | $(ffprobe -loglevel error -show_entries format_tags=artist -of default=noprint_wrappers=1:nokey=1 "$file")" >> data.txt
   fi
done
cp data.txt /mnt/c/Users/Kevin\ Liu/Desktop/ShellScriptPython
rm data.txt
cd /mnt/c/Users/Kevin\ Liu/Desktop/ShellScriptPython
python3 main.py
