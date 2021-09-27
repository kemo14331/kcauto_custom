#!/bin/bash

BASEDIR=$(dirname "$0")

$BASEDIR/configs/config_generator

python3.7 $BASEDIR/kcauto --cli --cfg config |& grep -v "scrot"