#! /bin/sh

# Copied wholesale from https://docs.aws.amazon.com/lambda/latest/dg/python-package-create.html#python-package-create-with-dependency

pip install --target ./package -r requirements.txt
(cd package && zip -r ../package.zip .)
zip -g package.zip playmaker.py
rm -r package