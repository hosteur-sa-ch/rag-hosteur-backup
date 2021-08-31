# Allow Sudoers script for restic 
#!/bin/bash

cat > /etc/sudoers.d/hosteur <<-EOM
        Cmnd_Alias RESTIC = /usr/bin/restic snapshot *, /usr/bin/restic backup *, /usr/bin/restic ls *, /usr/bin/restic find *, /usr/bin/restic restore *
        %ssh-access ALL = NOPASSWD: RESTIC
    EOM
chmod 440 /etc/sudoers.d/hosteur