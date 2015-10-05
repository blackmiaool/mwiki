import os;
if os.name=='posix':#linux
    download_path=r'./tiddlers';
    git_path=r'';
    cloud_path=r'/home/blackmiaool/Nutstore/mwiki/.git';
elif os.name=='nt':#windows
    download_path=r'C:\Users\blackmiaool\Downloads\\';
    git_path=r'C:\Users\blackmiaool\AppData\Local\GitHub\PortableGit_c2ba306e536fdf878271f7fe636a147ff37326ad\bin\\';