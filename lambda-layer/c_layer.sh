#!/usr/bin/env bash


while [[ "$#" -gt 0 ]]; do case $1 in
  -v|--version) pythonEnvs+=("$2"); shift;;
  -n|--layer-name) layerName="$2"; shift;;
  -d|--desc) layerDescription="$2"; shift;;
  *) echo "Unknown parameter passed: $1"; exit 1;;
esac; shift; done


# Create and install requirements to directory.
for penv in ${pythonEnvs[@]}; do
    mkdir -pv python/lib/${penv}/site-packages
    sudo docker run -v "$PWD":/var/task "lambci/lambda:build-${penv}" /bin/sh -c "pip install -r requirements.txt -t python/lib/${penv}/site-packages/ --upgrade ; exit"
done


# Create zip file of environments.
zip -r ${layerName}.zip python

exit
# Publish Layer to Lambda.
aws lambda publish-layer-version \
    --layer-name "${layerName}" \
    --description "${layerDescription}" \
    --zip-file "fileb://${layerName}.zip" \
    --compatible-runtimes ${pythonEnvs[@]}
