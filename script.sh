#!/bin/bash

source entorno/bin/activate

if pytest; then
    exit 0
else
    exit 1
fi
