from fabric.api import *
from time import sleep
from fabric.colors import red

env.use_ssh_config = True
env.sudo_prefix = "sudo -S -p '%(sudo_prompt)s' -H " % env

def production():
    env.host_string = "freedb.musicbrainz.org"
    no_local_changes()
    with cd("/home/mb2freedb/mb2freedb"):
        sudo("git pull --ff-only", user="mb2freedb")
        sudo("invoke-rc.d apache2 reload")

def no_local_changes():
    # The exit code of these will be 0 if there are no changes.
    # If there are changes, then the author should fix his damn code.
    with settings(hide("stdout")):
        local("git diff --exit-code")
        local("git diff --exit-code --cached")
