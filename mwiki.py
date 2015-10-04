import os,sys,time,re,shutil,distutils;

####### configuration #######
if os.name=='posix':#linux
    download_path=r'./tiddlers';
    git_path=r'';
    cloud_path=r'/home/blackmiaool/Nutstore/mwiki/.git';
elif os.name=='nt':#windows
    download_path=r'C:\Users\blackmiaool\Downloads\\';
    git_path=r'C:\Users\blackmiaool\AppData\Local\GitHub\PortableGit_c2ba306e536fdf878271f7fe636a147ff37326ad\bin\\';

wiki_name=r'mwiki';

# if you use github
use_github=1;
github_push_every=1 #times commit
# github configuration end

####### configuration end #######


####### init ########
mtime=0;
mtime_pre=0;
wait_next=0;
index=0;
pattern = re.compile(wiki_name+r'[ \S]*.html');
new_file_mtime=0;
try:
    use_github;
except NameError:
    use_github=0;
else:
    github_index=0;

try:
    cloud_path;
except NameError:
    cloud_path=0;
###################


def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)
    else:
        shutil.copyfile(src, dest)
while 1:
    if wait_next:
        time.sleep(1);
    else:
        time.sleep(0.5);
        statinfo=os.stat(download_path)
        mtime=statinfo.st_mtime;
    changed=0;

    if mtime!=mtime_pre:
        changed=1;
        mtime_pre=mtime;
    if wait_next:
        if not changed:                             
            index=index+1;
            os.system(git_path+'git add * > /dev/null');      
            os.system(git_path+'git commit -am "python auto commit" > /dev/null');
            if use_github:
                if not index%github_push_every:
                    os.system("git push");
            # if cloud_path:
            #     recursive_overwrite(".git",cloud_path)                        
            wait_next=0;
    else:
        if changed:
            wait_next=1;                        
