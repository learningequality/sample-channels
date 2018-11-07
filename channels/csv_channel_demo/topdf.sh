#!/usr/bin/env bash
set -e
# SETTINGS
################################################################################

MICROWAVE_HOST="http://35.185.105.222"
MICROWAVE_PORT="8989"
MICROWAVE_PATH="/unoconv/pdf"
MICROWAVE_URL="${MICROWAVE_HOST}:${MICROWAVE_PORT}${MICROWAVE_PATH}"

# INPUT PROCESSING
################################################################################
if [ -z "$1" ]; then
  echo -e "Missing command args. You must provide file path use the -d option  "
  echo -e "Usage:"
  echo -e "   ./topdf.sh DomeDir/somefile.docx   # --> SomeDir/somefile.pdf"
  echo -e " OR "
  echo -e "   ./topdf.sh -d  # convert all docx/pptx files in current dir and subdirs"
  exit 1
fi



if [ "$1" == "-d" ]
then  #### DIRECTORY MODE ######################################################

  echo "Processing all office files in current dir " `pwd`
  echo "A. Converting all DOCXs via microwave )))))))))))))))))))))))))))))))))"
  find . -name '*.docx'  -print0 | 
      while IFS= read -r -d $'\0' line;
      do 
          echo "  - converting $line";
          $0 "$line"
      done

  echo "B. Converting all PPTX  [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ]   [ ]  "
  find . -name '*.pptx'  -print0 | 
      while IFS= read -r -d $'\0' line;
      do 
          echo "   - converting $line";
          $0 "$line"
      done

else  #### FILE MODE ###########################################################

  FILENAME=$1  # path to file we want to process
  filename_noext="${FILENAME%.*}"
  ext="${FILENAME##*.}"
  OUTFILENAME="${filename_noext}.pdf"
  echo "$OUTFILENAME"
  # 
  if [ ! -f "$OUTFILENAME" ]
  then 
    echo "Running:"
    echo "curl --form file=@\"${FILENAME}\"  ${MICROWAVE_URL}  > ${OUTFILENAME}"
    curl --form file=@"${FILENAME}"  ${MICROWAVE_URL}  >  "$OUTFILENAME"
  fi


fi
