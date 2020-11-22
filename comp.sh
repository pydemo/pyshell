rm src.zip
zip -r src * -x layers/* -x .git -x lambda/*
ls -alh src.zip
