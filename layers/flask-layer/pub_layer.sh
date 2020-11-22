aws lambda publish-layer-version \
    --layer-name "flask-layer" \
    --description "Lambda Layer for Flask 1.1.1" \
    --zip-file "fileb://flask-layer.zip" \
    --compatible-runtimes "python3.7"
