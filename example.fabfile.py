# coding: utf-8
import os
from fabric.api import run, env, cd, roles, lcd, local, sudo

def gp(): #gp=git-push
    lcd('projects/dmg/')
    local('sudo git add .')
    local('sudo git commit -a')
    local('sudo git push origin1 master')
