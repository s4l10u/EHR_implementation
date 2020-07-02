#!/bin/bash

$( git add .)

read -p  'message for commit ' mes
$( git commit -m '{$mes}' ) 