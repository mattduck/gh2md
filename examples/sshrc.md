Export of Github issues for [Russell91/sshrc](https://github.com/Russell91/sshrc). Generated on 2017.05.20 at 19:19:02.

# [\#86 PR](https://github.com/Russell91/sshrc/pull/86) `open`: improve readme.md

#### <img src="https://avatars2.githubusercontent.com/u/2073458?v=3" width="50">[Benedikt Heine](https://github.com/bebehei) opened issue at [2017-03-17 23:45](https://github.com/Russell91/sshrc/pull/86):

Looking over your nice project.

But sorry, I couldn't resist correcting this ugly code.




-------------------------------------------------------------------------------

# [\#85 PR](https://github.com/Russell91/sshrc/pull/85) `open`: Use base64 from coreutils for encoding and decoding

#### <img src="https://avatars0.githubusercontent.com/u/5731555?v=3" width="50">[Michał Leśniewski](https://github.com/mlesniew) opened issue at [2017-03-10 14:07](https://github.com/Russell91/sshrc/pull/85):

The data transferred to the remote servers is encoded using base64.
This commit changes the tool used to encode and decode the data from
openssl to the base64 utility.

The change was done because openssl may be missing on some systems while
base64 should always be installed as it is part coreutils.  Moreover,
openssl needs to access openssl.cnf, which is usually located somewhere
under /etc.  This part of the file system may not be accessible to the
user on some remote machines, so openssl could fail in these cases.




-------------------------------------------------------------------------------

# [\#84 PR](https://github.com/Russell91/sshrc/pull/84) `open`: Deduplicate bash config file setup

#### <img src="https://avatars0.githubusercontent.com/u/2508427?v=3" width="50">[taylorskalyo](https://github.com/taylorskalyo) opened issue at [2017-02-15 03:47](https://github.com/Russell91/sshrc/pull/84):

Deduplicate bash config file setup and try to fix indentation

To see the changes with whitespace ignored, you can add [`?w=1`](https://github.com/blog/967-github-secrets) to the URL: https://github.com/Russell91/sshrc/compare/master...taylorskalyo:deduplicate_bash_conf?w=1




-------------------------------------------------------------------------------

# [\#83 PR](https://github.com/Russell91/sshrc/pull/83) `open`: run `cat /etc/motd` or `run-parts /etc/motd.d`, not both

#### <img src="https://avatars0.githubusercontent.com/u/2508427?v=3" width="50">[taylorskalyo](https://github.com/taylorskalyo) opened issue at [2017-02-15 03:46](https://github.com/Russell91/sshrc/pull/83):

Running both commands often results in the message of the day being shown twice.




-------------------------------------------------------------------------------

# [\#82 PR](https://github.com/Russell91/sshrc/pull/82) `open`: alpine mktemp compatible

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) opened issue at [2017-02-13 05:42](https://github.com/Russell91/sshrc/pull/82):

mktemp in alpine require at least  six X

```bash
bash-4.3$ mktemp -d -t .$(whoami).sshrc.XXXXXX
/tmp/.dev.sshrc.cbGnFl
bash-4.3$ mktemp -d -t .$(whoami).sshrc.XXXX
mktemp: Invalid argument
```




-------------------------------------------------------------------------------

# [\#79 Issue](https://github.com/Russell91/sshrc/issues/79) `open`: executing a script before .bash_profile ...

#### <img src="https://avatars3.githubusercontent.com/u/198502?v=3" width="50">[Victor Volle](https://github.com/kontrafiktion) opened issue at [2016-12-20 13:03](https://github.com/Russell91/sshrc/issues/79):

I love to switch on coloured prompts. 
Most default .bashrc contain a switch "force_color_prompt=yes", but this has to be set
before the .bashrc is sourced. So I would like to have a script that is sourced before .bashrc is sourced.

I currently just added 

    export force_color_prompt=yes

before

    if [ -r /etc/profile ]; then source /etc/profile; fi
    ...

but I would love a solution where I do not have to patch `sshrc` itself




-------------------------------------------------------------------------------

# [\#78 Issue](https://github.com/Russell91/sshrc/issues/78) `open`: Loading rc files was failed after ssh reconnected with tmux attach

#### <img src="https://avatars1.githubusercontent.com/u/4897842?v=3" width="50">[aiya000](https://github.com/aiya000) opened issue at [2016-12-11 00:52](https://github.com/Russell91/sshrc/issues/78):

The shell cannot loads rc files in this case :sob:  

- First

```console
$ sshrc (foo_host)
$ tmux
(And resume tmux)
$ exit
(Leave remote host)
```

- Second

```console
$ sshrc (foo_host)
$ tmux attach
(And create new tab with starting bash)
--> !!! Bash was started without loading .bashrc and .bash_profile
```

- - -

I think it's better to be able to lock $SSHHOME :smile:




-------------------------------------------------------------------------------

# [\#77 Issue](https://github.com/Russell91/sshrc/issues/77) `open`: sshrc doesn't work when remote user's default shell isn't `bash`

#### <img src="https://avatars1.githubusercontent.com/u/4512269?v=3" width="50">[Kirill Rogovoy](https://github.com/kirillrogovoy) opened issue at [2016-11-20 19:29](https://github.com/Russell91/sshrc/issues/77):

I'm trying to use `sshrc` logging in as a user with `fish` default shell instead of `bash`.
The `ssh -t` commands are executed by fish instead of bash hence I have a syntax error and `sshrc` doesn't work.

To reproduce it:

1. Make a new user at the remote server (or at your local PC in case you have a SSH server installed)
1. Install `fish`
1. Run `chsh -s $(which fish)` by that user
1. Log in by another user
1. Run `echo "exec \$SHELL" > ~/.sshrc`
1. Run `sshrc user@host`

Can you fix it or is there a workaround for this issue?
Perhaps, the best way might be to add `bash -c` at the beginning of the `ssh -t` script (https://github.com/Russell91/sshrc/blob/master/sshrc#L25).




-------------------------------------------------------------------------------

# [\#76 PR](https://github.com/Russell91/sshrc/pull/76) `open`: Avoid warnings caused by BSD tar vs. GNU tar

#### <img src="https://avatars0.githubusercontent.com/u/233589?v=3" width="50">[Daniel Serodio](https://github.com/dserodio) opened issue at [2016-10-27 16:53](https://github.com/Russell91/sshrc/pull/76):

When using sshrc to ssh from Mac to Linux, I get:

```
tar: Ignoring unknown extended header keyword `SCHILY.dev'
tar: Ignoring unknown extended header keyword `SCHILY.ino'
tar: Ignoring unknown extended header keyword `SCHILY.nlink'
tar: Ignoring unknown extended header keyword `SCHILY.dev'
tar: Ignoring unknown extended header keyword `SCHILY.ino'
tar: Ignoring unknown extended header keyword `SCHILY.nlink'
```

This PR silences these warnings that are caused by creating the
tar with BSD tar and extracting it with GNU tar.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-11-20 00:54](https://github.com/Russell91/sshrc/pull/76#issuecomment-261750507):

Are other people getting this issue? I was unable to accept because the `--warning=no-unknown-keyword` flag is not imlemented elsewhere. But we could try to get clever if necessary.

#### <img src="https://avatars1.githubusercontent.com/u/748652?v=3" width="50">[Georgy Krasulya](https://github.com/gkrasulya) commented at [2017-02-06 20:13](https://github.com/Russell91/sshrc/pull/76#issuecomment-277799298):

Hello. You can try this:
```
brew install gnu-tar
sudo ln -s `which gtar` /usr/local/bin/tar
```
Make sure that `which tar` is "/usr/local/bin/tar" and try logging on remote server


-------------------------------------------------------------------------------

# [\#75 PR](https://github.com/Russell91/sshrc/pull/75) `open`: Use $0 to determine if the user want ssh or mosh

#### <img src="https://avatars3.githubusercontent.com/u/2104672?v=3" width="50">[Hugues Morisset](https://github.com/izissise) opened issue at [2016-10-06 21:51](https://github.com/Russell91/sshrc/pull/75):

Remove moshrc script as it is out of sync
Everything in one script to aid maintainability

```
ln -s sshrc moshrc
./moshrc
```





-------------------------------------------------------------------------------

# [\#74 Issue](https://github.com/Russell91/sshrc/issues/74) `open`: sshrc doesn't work due to missing mktemp and -z flag on tar

#### <img src="https://avatars3.githubusercontent.com/u/2356012?v=3" width="50">[Δημήτρης Ραβιόλος](https://github.com/DictumMortuum) opened issue at [2016-08-23 09:11](https://github.com/Russell91/sshrc/issues/74):

```
ksh[10]: mktemp:  not found
Permission denied
ksh[13]: /sshrc: cannot create
chmod: /sshrc: No such file or directory
Permission denied
ksh[16]: /sshrc.bashrc: cannot create
Permission denied
ksh[18]: /bashsshrc: cannot create
chmod: /bashsshrc: No such file or directory
Usage: tar -{c|r|t|u|x} [ -BdDEFhilmopRsUvwZ ] [ -Number ] [ -f TarFile ]
           [ -b Blocks ] [ -S [ Feet ] | [ Feet@Density ] | [ Blocksb ] ]
           [ -L InputList ] [-X ExcludeFile] [ -N Blocks ] [ -C Directory ] File ...
Usage: tar {c|r|t|u|x} [ bBdDEfFhilLXmNopRsSUvwZ[0-9] ]
           [ Blocks ] [ TarFile ] [ InputList ] [ ExcludeFile ] 
           [ [ Feet ] | [ Feet@Density ] | [ Blocksb ] ] [-C Directory ] File ...
Permission denied
ksh[23]: /sshrc.bashrc: cannot create
```

Would it be possible to add a pure-bash implementation of mktemp to sshrc? Something like [this](https://github.com/vlisivka/bash-modules/blob/master/main/bash-modules/src/bash-modules/mktemp.sh) implementation.

The -z tar could be solved by piping to gzip, but I didn't read thoroughly the code for all tar commands. 


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-09-03 06:34](https://github.com/Russell91/sshrc/issues/74#issuecomment-244530339):

Interesting. What are your system details?

#### <img src="https://avatars3.githubusercontent.com/u/2356012?v=3" width="50">[Δημήτρης Ραβιόλος](https://github.com/DictumMortuum) commented at [2016-09-03 08:14](https://github.com/Russell91/sshrc/issues/74#issuecomment-244533892):

This occurs on an old AIX informix database machine that we use at work.

Apparently, it uses KSH as its login shell, but everyone just changes to BASH and sources a configuration file that sets up environment variables to access the database.

As one database machine can host multiple database servers, I was looking to use ssh_config to speed up things by having virtual hostnames pointing to the same server and then using sshrc to source the correct configs server-side.


-------------------------------------------------------------------------------

# [\#72 Issue](https://github.com/Russell91/sshrc/issues/72) `closed`: Execute command (or, generalizing: support profiles)

#### <img src="https://avatars0.githubusercontent.com/u/2845433?v=3" width="50">[memeplex](https://github.com/memeplex) opened issue at [2016-08-01 17:29](https://github.com/Russell91/sshrc/issues/72):

I use ssh to execute remote psql shells: `ssh -t myserver psql ...`. I would like to configure readline using sshrc to upload my .inputrc. But sshrc expands `$@` _before_ doing its stuff, which is usually fine because `$@` will consist of host information and ssh options, not remote commands. Do you think adding the possibility of executing a command _after_ setting the remote environment will be worth the extra complexity in the cli?

A more general approach, akin to the way sshrc currently copes with per-server profiles, is to execute sshrc like `SSHRCPROFILE=psql sshrc myserver` where `SSHRCPROFILE` will be propagated to the remote environment thus allowing .sshrc to act according not only to a hostname or another bit of information characterizing the remote host but also to some state (the profile) established while launching it.

I think this second approach is simple to implement and very flexible.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-08-03 20:55](https://github.com/Russell91/sshrc/issues/72#issuecomment-237370519):

It seems like implementing the `-t` option would actually solve this issue, right? This is something I've been meaning to do, but haven't found a good way of doing simply yet.

#### <img src="https://avatars0.githubusercontent.com/u/2845433?v=3" width="50">[memeplex](https://github.com/memeplex) commented at [2016-08-03 21:05](https://github.com/Russell91/sshrc/issues/72#issuecomment-237373352):

I'm not sure I'm following you but the command argument doesn't sit next to `-t`. Finding the command implies a more complex parsing of the command line. I like the profile approach most, first because of its generality, second because of its consistency with what sshrc currently does in order to target different servers, third because the environment variable technique avoids having to parse the complex command line of ssh.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-08-03 21:20](https://github.com/Russell91/sshrc/issues/72#issuecomment-237377863):

Well, 1) having the `-t` would let you just do `sshrc myserver -t "export MYENV='$MYENV'"` for any variable, so it would solve that problem. But it is indeed way more complex. That being said, we were considering adding it anyway for consistence with ssh.

Edit:
But I guess you're saying that the problem is you want to be able to set that SSHRCPROFILE in your e.g. bashrc and have it be read in every time that you run sshrc?

#### <img src="https://avatars0.githubusercontent.com/u/2845433?v=3" width="50">[memeplex](https://github.com/memeplex) commented at [2016-08-03 21:27](https://github.com/Russell91/sshrc/issues/72#issuecomment-237379872):

Regarding implementing `-t`, if that means supporting remote execution from the command line as in ssh, all I'm saying is that it's more difficult to implement because you have to deal with the ssh cli. That said, if you are implementing that anyway, it will surely solve the issue. I don't care about exporting some profile variable per se, it was just a way to simplify things.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-08-07 23:33](https://github.com/Russell91/sshrc/issues/72#issuecomment-238116104):

Okay, how does the version [here](https://github.com/Russell91/sshrc/blob/command/sshrc) work for you?

#### <img src="https://avatars0.githubusercontent.com/u/2845433?v=3" width="50">[memeplex](https://github.com/memeplex) commented at [2016-08-08 18:38](https://github.com/Russell91/sshrc/issues/72#issuecomment-238334602):

Seems to work fine!


-------------------------------------------------------------------------------

# [\#71 Issue](https://github.com/Russell91/sshrc/issues/71) `closed`: Turn off motd

#### <img src="https://avatars0.githubusercontent.com/u/5013883?v=3" width="50">[Timmo Verlaan](https://github.com/tverlaan) opened issue at [2016-07-26 06:48](https://github.com/Russell91/sshrc/issues/71):

It would be nice to turn off the motd like `.hushlogin` usually does. However since this is focused on the client we should have a local `.hushlogin` or `.remotehushlogin` of some sorts. I'd be willing to implement this but there is no system in place that offers configuration and therefor I'm looking for feedback. I saw the `-t` in the dev branch, but I'm not sure if that's the way to go (why would you need sshrc anyway if just executing one command?). If `-t` is really coming we could add `-q` for 'quiet'.

Another possibility is to remove the motd and last login stuff and leave it up to the user (add example to readme). However this breaks backwards user experience :-).

I'd love some feedback on this.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-08-07 23:50](https://github.com/Russell91/sshrc/issues/71#issuecomment-238116972):

Okay, this capability is added in the latest [command branch](https://github.com/Russell91/sshrc/blob/command/sshrc). I added support for the .hushlogin on the server as ssh does, and I also added your second suggestion such that you can type

```
touch ~/.sshrc.d/.hushlogin
```

on your local machine and this will apply across all of the servers you sshrc into! I am going to use this myself as I agree that the login messages are an annoyance. Sound good?


-------------------------------------------------------------------------------

# [\#69 Issue](https://github.com/Russell91/sshrc/issues/69) `closed`: sshrc fails to transfer all files on one particular remote machine

#### <img src="https://avatars2.githubusercontent.com/u/2192679?v=3" width="50">[swiftster](https://github.com/swiftster) opened issue at [2016-06-29 18:41](https://github.com/Russell91/sshrc/issues/69):

I'm having trouble getting sshrc to work on one remote machine. It works fine on my other servers running Debian GNU/Linux 8 (jessie).

It seems the transfer doesn't complete. I tried reading your script to see if I could isolate the transfer to see if I could understand why it was failing, but the code is over my head.

**Local**: Mac OS 10.10.5; sshrc installed with brew (version 0.6.1)
**Remote**: Ubuntu 16.04 LTS (GNU/Linux 4.4.0-24-generic x86_64)

**Error Message**
gzip: stdin: unexpected end of file
tar: Child returned status 1
tar: Error is not recoverable: exiting now

**Other Info**

echo $$SSHOME
/tmp/.sswift.sshrc.ZJOw
ls $$SSHOME
bashsshrc  sshrc  sshrc.bashrc

These are all empty files.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-07-09 17:18](https://github.com/Russell91/sshrc/issues/69#issuecomment-231545142):

Can you confirm whether the error is on the local or the remote machine? I don't have a 16.04 machine to test on at the moment, but it would be great if someone with one could make sure this problem doesn't reoccur for any remote 16.04 machine.

#### <img src="https://avatars2.githubusercontent.com/u/2192679?v=3" width="50">[swiftster](https://github.com/swiftster) commented at [2016-07-12 15:53](https://github.com/Russell91/sshrc/issues/69#issuecomment-232092580):

Well, I feel a little silly. The problem was my shell was sh (someone else set up this computer and my account).

Changed my default shell to bash, and all is well.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-07-12 20:04](https://github.com/Russell91/sshrc/issues/69#issuecomment-232162819):

I see, glad you got it figured out!


-------------------------------------------------------------------------------

# [\#68 Issue](https://github.com/Russell91/sshrc/issues/68) `closed`: Support for GPG?

#### <img src="https://avatars1.githubusercontent.com/u/5354184?v=3" width="50">[Zakatell KANDA](https://github.com/zkanda) opened issue at [2016-05-19 06:19](https://github.com/Russell91/sshrc/issues/68):

Hello, Is there any way I can use `sshrc` to temporarily copy and use my gpg key to the server?
My use case:
1. Sometimes I connect to a server a fix something there.
2. I want to commit this changes but sign it with my key.

Thank you.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-05-19 22:15](https://github.com/Russell91/sshrc/issues/68#issuecomment-220467534):

Yea, just put your gpg key into the ~/.sshrc.d folder and you can access it at $SSH_HOME/.sshrc.d/gpg.key on the remote machin.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-05-24 06:34](https://github.com/Russell91/sshrc/issues/68#issuecomment-221178920):

Did this answer your question?

#### <img src="https://avatars1.githubusercontent.com/u/5354184?v=3" width="50">[Zakatell KANDA](https://github.com/zkanda) commented at [2016-05-24 07:34](https://github.com/Russell91/sshrc/issues/68#issuecomment-221189188):

Yes it does, thanks for closing it. :+1:


-------------------------------------------------------------------------------

# [\#66 Issue](https://github.com/Russell91/sshrc/issues/66) `closed`: Feedback / code review on new "-t" option
**Labels**: `help wanted`


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2016-05-04 02:39](https://github.com/Russell91/sshrc/issues/66):

The sshrc in the dev branch (https://github.com/Russell91/sshrc/blob/dev/sshrc) has a new -t option, which will append the argument following -t as a new line to a copy of the .sshrc file, and exit after running command. Do people have any thoughts on this?


#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-05-05 10:33](https://github.com/Russell91/sshrc/issues/66#issuecomment-217120923):

I like the concept.   Could it be done in the same way as ssh though ?   where it doesn't need a "-t" flag, simply whatever is after the host name is passed to the server as a command.   All the other commands commands / args are the same as the default ssh, so it makes sense to me to deal with the "comand" in the same way as ssh deals with it.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-05-05 19:11](https://github.com/Russell91/sshrc/issues/66#issuecomment-217247221):

Yea, that's a good point. It should be done that way. We'll need to emulate the sshrc argument parser though.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-05-06 08:55](https://github.com/Russell91/sshrc/issues/66#issuecomment-217388880):

How about something along the lines of ....

```
DOMAIN=""
SSHARGS=""
CMNDARG=""
while [[ -n $1 ]]; do
  case $1 in
    -h | --help)
      echo "some nice help message" ; exit ;;
    -b | -c | -D | -E | -e | -F | -I | -i | -L | -l | -m | -O | -o | -p | -Q | -R | -S | -W | -w )
      SSHARGS="$SSHARGS $1 $2"; shift ;;
    -t )
      echo "-t not allowed with sshrc"; exit ;;
    -* )
      SSHARGS="$SSHARGS $1" ;;
    *)
      if [ -z $DOMAIN ]; then
       DOMAIN="$1"
      else
        CMNDARG="$CMNDARG $1"
      fi
      ;;
  esac
  shift
done
```

Which would then provide you with 
- the ssh options (SSHARGS) that you could pass on to ssh, 
- the domain name (DOMAIN), and
- the CMNDARG with any command to be passed ( ideally there should be only one, quoted, but this allows multiple) 

It also enables;
- the -h / --help flag for you to provide a default help message about sshrc usage and
- blocks the -t flag from being passed to ssh separately to the -t flag that sshrc is using.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-07-25 18:46](https://github.com/Russell91/sshrc/issues/66#issuecomment-235046494):

I really don't like explicitly casing on all this stuff for backwards compat reasons. It also just complicates the entire script. Isn't there some way we could accomplish this with fewer lines of code?

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-07-26 19:24](https://github.com/Russell91/sshrc/issues/66#issuecomment-235376887):

The explicit casing was purely because that's the explicit casing that SSH uses. 

Yes, could be shorter, it's always a balance between compactness and readability I think.   It depends which is more important.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-08-07 23:33](https://github.com/Russell91/sshrc/issues/66#issuecomment-238116082):

Okay, thoughts on the new version at https://github.com/Russell91/sshrc/blob/command/sshrc?

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-08-08 06:54](https://github.com/Russell91/sshrc/issues/66#issuecomment-238155442):

works for me :) 

Personally I like the -h option ( to provide a little help and guidance about the script)

If I was getting fussy, I'd say you might want to trap the "-W" and "-T" options, as they will cause it to hang / fail.  I suspect the chances of anyone trying to use the options, with your script, are very remote though.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-08-08 21:04](https://github.com/Russell91/sshrc/issues/66#issuecomment-238377031):

Okay, I'll consider doing something for the -h in the future. Good points about -T and -W, but looking at the use cases it seems anyone trying them with sshrc would not expect them to work in the first place. So I don't think it's necessary to add the code.


-------------------------------------------------------------------------------

# [\#65 Issue](https://github.com/Russell91/sshrc/issues/65) `closed`: Please make latest tag and release

#### <img src="https://avatars1.githubusercontent.com/u/4200911?v=3" width="50">[Ikuo Degawa](https://github.com/ikuwow) opened issue at [2016-04-29 09:40](https://github.com/Russell91/sshrc/issues/65):

Probably 0.6.1?

I think recent changes relating to xxd (The message: `sshrc requires xxd to be installed on the server, but it's not. Aborting.`) should be distributed by homebrew.

https://github.com/Russell91/sshrc/commits/master
https://github.com/Homebrew/homebrew-core/blob/fb81645562f7e495a49561065912788af2d1f14f/Formula/sshrc.rb


#### <img src="https://avatars2.githubusercontent.com/u/2143908?v=3" width="50">[Stephen Ball](https://github.com/REBELinBLUE) commented at [2016-05-01 20:57](https://github.com/Russell91/sshrc/issues/65#issuecomment-216072266):

I was just about to ask exactly the same thing

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-05-01 21:14](https://github.com/Russell91/sshrc/issues/65#issuecomment-216073152):

Okay, done! For the record, the delay between master and tagged releases for homebrew etc. is done to help reduce the effect of potential bugs.

#### <img src="https://avatars1.githubusercontent.com/u/4200911?v=3" width="50">[Ikuo Degawa](https://github.com/ikuwow) commented at [2016-05-04 03:23](https://github.com/Russell91/sshrc/issues/65#issuecomment-216732626):

Thank you! I submitted pull request to homebrew-core:
https://github.com/Homebrew/homebrew-core/pull/828


-------------------------------------------------------------------------------

# [\#61 Issue](https://github.com/Russell91/sshrc/issues/61) `closed`: Is it possible to add a surc

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) opened issue at [2016-04-09 07:33](https://github.com/Russell91/sshrc/issues/61):

surc is just su + sshrc's rc files.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-09 20:48](https://github.com/Russell91/sshrc/issues/61#issuecomment-207852235):

You would have to spend at least a little more effort explaining the virtues of adding this. But the answer is likely going to be no.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-04-11 13:46](https://github.com/Russell91/sshrc/issues/61#issuecomment-208351535):

The key virtue to me is when logging into a server as a non privileged user and then wanting to "sudo su" to change to the root user for admin tasks.     I had a look into automating it, however there was usually some undesired feature that came with each method I tried.   In the end I resulted to simply doing 

. /tmp/.user.sshrc. (where "user" is your normal username, and pressing tab to auto-complete followed by .sshrc )    

This then ran my usual sshrc files and gave me all my normal configuration / functions etc as su.    Since there was no need to code / modify anything, just a simple command - I used that.

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) commented at [2016-04-11 16:17](https://github.com/Russell91/sshrc/issues/61#issuecomment-208431929):

I can't access `/tmp/.user.sshrc.` due to permission denied. I `sshrc root@host` then `su other`.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-04-11 16:55](https://github.com/Russell91/sshrc/issues/61#issuecomment-208448490):

I'm not sure I see any advantages of adding all the sshrc functions that way round. 

It would be relatively easy to create a surc script though that placed the relevant files in a location that the new user did have permission to read, then simply run the file in that location once you are set as the new user.   The script should tidy up the file you created afterwards.

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) commented at [2016-04-11 16:59](https://github.com/Russell91/sshrc/issues/61#issuecomment-208449537):

Thanks, I will use the source to load my sshrc from other user.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-20 17:40](https://github.com/Russell91/sshrc/issues/61#issuecomment-212530430):

Okay @wenerme, looks like you were able to figure this out?

#### <img src="https://avatars2.githubusercontent.com/u/2143908?v=3" width="50">[Stephen Ball](https://github.com/REBELinBLUE) commented at [2016-04-21 12:43](https://github.com/Russell91/sshrc/issues/61#issuecomment-212901705):

@wenerme Did you ever come up with an automated way of doing this? I am after something similar myself for vagrant machines where I need to `su` but I am not able to change the provisioning script to change the profile for other users. Currently I am just running `chmod -r 777 /tmp/.stephen.XXX/` then changing the user and doing `source /tmp/.stephen.XXXX/.sshrc` but was looking to see if anyone had automated it

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) commented at [2016-04-21 13:13](https://github.com/Russell91/sshrc/issues/61#issuecomment-212913393):

@REBELinBLUE Sorry I don't have a solution now. I think `surc` should `chmod` to target user.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-04-21 13:20](https://github.com/Russell91/sshrc/issues/61#issuecomment-212916559):

It depends if you just want root permissions ( su ) or if you want to completely represent a different user ( with some additional sshrc from your script)

If you want to just have the permissions of superuser ( or a different user) then you could simply do
sudo -E su -p (user) 
which preserves your environment.   However, as it preservers your environment it keeps environmental variables such as  $HOME pointing you your 'real' home directory, not the user you are trying to become.  

You could have a simple script that you could run which would update the relevant variables such as HOME though. (simply check if SUDO_COMMAND exists, if so then set the HOME variable from that).


-------------------------------------------------------------------------------

# [\#60 Issue](https://github.com/Russell91/sshrc/issues/60) `closed`: Alternatives to xxd

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) opened issue at [2016-04-08 10:45](https://github.com/Russell91/sshrc/issues/60):

I see from old closed issues that there has been some talk of providing alternatives to xxd.    I found it wasn't on all the servers I connected to. 

I tested by creating variables for the encode / decode 
# xxd works fine if xxd is on the remote server

encodefn="xxd -p"
decodefn="xxd -p -r"
# uuencode works fine if uudecode is on the remote server

encodefn="uuencode -m - "
decodefn="uudecode"
# openssl works fine (and was on all of my servers)

encodefn="openssl enc -base64"
decodefn="openssl enc -d -base64"

Is there a desire to include alternatives ? if so I'm happy to produce a version that could either automatically fail over to using a different method, or could have a command line arg  ( e.g. -x, -u or -o for xxd, uuencode, openssl) 


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-08 19:00](https://github.com/Russell91/sshrc/issues/60#issuecomment-207559017):

Indeed https://github.com/Russell91/sshrc/pull/56 and https://github.com/Russell91/sshrc/pull/14 showed a lot of interest in changing away from xxd. I spent several hours trying to hack base64 into working, but the issue with that tool in particular is that it cannot support OSX and Linux simultaneously due to API versioning. I was not aware of openssl or uuencode prior to this post, so these could be promising substitutes. The minimal constraint on a pull request is that the tool needs to be able to work on both OSX and Debian. Emphasis on client side being good for OSX and server side being good for Debian. For now, the PR could try to automatically use one of these tools, and fall back to the xxd error message if none of the options works.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-04-08 19:21](https://github.com/Russell91/sshrc/issues/60#issuecomment-207566884):

I also tested using "base64" to encode on my laptop ( ubuntu - debian based ) and "openssl enc -d -base64" to decode on the server - that worked perfectly as well. 

I don't have easy access to OSX to test those - so can't verify those I'm afraid.

uuencode / uudecode worked fine - but tended to be on the older servers for me, rather than the newer ones.   openssl was on all of the ones I tested though ( debian and redhat / centos )  and was consistent across all ( for me ).

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-08 19:33](https://github.com/Russell91/sshrc/issues/60#issuecomment-207571035):

I see. The problem with OSX is that Steve Jobs stopped accepting new UNIX tools due to GPL concerns.  But OSX Server is going to be incredibly uncommon, so if you want to do a server side only pull request adding support for these tools, that would be great. Maybe we could make it so that one would also transfer a few bytes of verification (e.g. 'sshrc') at the beginning of the command and read those off from the decoding tool to make sure there are no incompatibilities in the base64/base16 encodings. But yea, if there were a little module that would look for any one of these tools, guarantee compatibility by making sure encoding . decoding == identity, and never exit with an xxd OR base64 OR ... error otherwise, that would be a strict win. Client side modifications would just have to be done by someone with a macbook.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-04-08 19:42](https://github.com/Russell91/sshrc/issues/60#issuecomment-207573885):

Sounds a good plan.  

I've just created a fork, and uploaded my test version at https://github.com/srvrco/sshrc/blob/test_alternates/sshrc if you have access to OSX and could test any  ( would like to see if some do work, before setting up the failover etc. )   it's not ready for a formal PR yet, but at least you could do a test before I tidy things up ( I changed a few things as I was working out how it all works ;)  )

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-09 20:49](https://github.com/Russell91/sshrc/issues/60#issuecomment-207852274):

Okay, I have this on my list of things to look into.

#### <img src="https://avatars3.githubusercontent.com/u/16167200?v=3" width="50">[serverco](https://github.com/srvrco) commented at [2016-04-11 12:22](https://github.com/Russell91/sshrc/issues/60#issuecomment-208314071):

Having played with this, I haven't found a realistic way to get it to chose the optimal conversion package with a single connection (because you need to know the encode method to send the files at the beginning, before you have determined which is the best method. 

The options that come to mind are; 
1.   Allow multiple connections - doing first a series of connections testing if the encoding / decoding method works.  I don't really like multiple connections each time though.
2.  Encode the data using all the available methods (from your PC) and then test to determine which decrypts best, and use that one.    This has the advantage of only one connection, however has the disadvantage of sending the data 3 times ( if using base64/openssl, xxd and uuencode ) 
3.  Allow a command line argument ( or config file ) for the user to specify which encoding method is used.  It could be a mixture of the two - a config file that allows you to specify your preferred default, and a command line argument that enables you to overwrite the default for certain connections.  

I'm open to other suggestions, I just wanted to put down my findings so far - and see if you had a preference for any of these options ( or an alternative solution )

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-26 00:09](https://github.com/Russell91/sshrc/issues/60#issuecomment-214568802):

Addressed by https://github.com/Russell91/sshrc/pull/64


-------------------------------------------------------------------------------

# [\#59 Issue](https://github.com/Russell91/sshrc/issues/59) `closed`: Sourced resources are not being transferred

#### <img src="https://avatars1.githubusercontent.com/u/661220?v=3" width="50">[Elvis](https://github.com/mu3) opened issue at [2016-04-06 06:41](https://github.com/Russell91/sshrc/issues/59):

I want to have some file with common settings for both local and remote environments.

```
[[ -f ~/.shared_rc ]] && . ~/.shared_rc
# Remote specific settings
exec -l $(which zsh) # invoke remote zsh shell
```

I believe this done for security reasons but maybe I'm missing something 🤔


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-06 20:51](https://github.com/Russell91/sshrc/issues/59#issuecomment-206561541):

It's not clear exactly what you're asking for. But any files you put into ~/.sshrc.d will be transferred to the remote environment, and they'll be accessible locally as well. Does that help?

So, for example, create ~/.sshrc.d/.shared_rc, and add 

```
source ~/.sshrc.d/.shared_rc
```

to your local .bashrc, and add

```
source $SSHHOME/.sshrc.d/.shared_rc
```

to your .sshrc.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-09 20:49](https://github.com/Russell91/sshrc/issues/59#issuecomment-207852301):

Marking as resolved for now. Hope it helped!


-------------------------------------------------------------------------------

# [\#58 Issue](https://github.com/Russell91/sshrc/issues/58) `closed`: Homebrew install moshrc

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) opened issue at [2016-03-26 16:22](https://github.com/Russell91/sshrc/issues/58):

Currently there is no moshrc in brew

```
$ brew info sshrc
sshrc: stable 0.5, HEAD
Bring your .bashrc, .vimrc, etc. with you when you SSH
https://github.com/Russell91/sshrc
/usr/local/Cellar/sshrc/0.5 (4 files, 7.1K) *
  Built from source
From: https://github.com/Homebrew/homebrew/blob/master/Library/Formula/sshrc.rb

$ brew info moshrc
Error: No available formula with the name "moshrc"

$ tree `brew --prefix sshrc`
/usr/local/opt/sshrc
├── INSTALL_RECEIPT.json
├── LICENSE
├── README.md
└── bin
    └── sshrc

1 directory, 4 files
```


#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) commented at [2016-03-26 16:28](https://github.com/Russell91/sshrc/issues/58#issuecomment-201883556):

Just need a new release tag.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-03-26 19:03](https://github.com/Russell91/sshrc/issues/58#issuecomment-201911979):

Okay, new release at https://github.com/Russell91/sshrc/releases/tag/0.6. Is there anything else I need to do?

#### <img src="https://avatars1.githubusercontent.com/u/1777211?v=3" width="50">[陈杨文](https://github.com/wenerme) commented at [2016-03-27 06:06](https://github.com/Russell91/sshrc/issues/58#issuecomment-201999412):

Thanks, that's enough, https://github.com/Homebrew/homebrew/pull/50453

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-03-28 06:21](https://github.com/Russell91/sshrc/issues/58#issuecomment-202255778):

Great! I don't use moshrc currently, but I know `brew install sshrc` is very convenient for me. Good work.


-------------------------------------------------------------------------------

# [\#57 PR](https://github.com/Russell91/sshrc/pull/57) `open`: Add screen config example to README.md

#### <img src="https://avatars1.githubusercontent.com/u/577441?v=3" width="50">[exAspArk](https://github.com/exAspArk) opened issue at [2016-01-29 16:47](https://github.com/Russell91/sshrc/pull/57):

To close #36. Based on the [tmux configuration](https://github.com/Russell91/sshrc#tmux).





-------------------------------------------------------------------------------

# [\#54 Issue](https://github.com/Russell91/sshrc/issues/54) `closed`: Having to specify full path to /usr/local/bin/sshrc even though its in PATH, and +x

#### <img src="https://avatars1.githubusercontent.com/u/3039509?v=3" width="50">[Predatorian](https://github.com/predatorian3) opened issue at [2015-10-02 16:46](https://github.com/Russell91/sshrc/issues/54):

For some reason, on CentOS 7, I'm having issues with this script running when its in /usr/local/bin/sshrc and set to 755. Then I changed the ownership from root to the user, and the user still cannot run it from the command line. However, specifying the full path allows it to run. Am I doing something wrong? 


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-10-12 07:40](https://github.com/Russell91/sshrc/issues/54#issuecomment-147312704):

Do you have a reason to believe that this issue would be caused by sshrc rather than you PATH and permission settings of the OS?

#### <img src="https://avatars1.githubusercontent.com/u/3039509?v=3" width="50">[Predatorian](https://github.com/predatorian3) commented at [2015-10-13 13:08](https://github.com/Russell91/sshrc/issues/54#issuecomment-147709139):

Yes, I was mistaken. My apologies, this can be closed.


-------------------------------------------------------------------------------

# [\#53 Issue](https://github.com/Russell91/sshrc/issues/53) `closed`: Last login information

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2015-09-18 05:34](https://github.com/Russell91/sshrc/issues/53):

Request for comment on how to emulate ssh's output when logging in e.g.

Last login: Thu Sep 17 22:32:11 2015 from 000.000.000.000


#### <img src="https://avatars3.githubusercontent.com/u/999845?v=3" width="50">[Jonathan Rehm](https://github.com/jkrehm) commented at [2015-09-18 19:55](https://github.com/Russell91/sshrc/issues/53#issuecomment-141551314):

I was looking into that a week or so ago and found a forum post that gave me this much:

`lastlog -u $USER | sed -n "2{p;q}" | tr -s ' ' | cut -d' ' -f4-9`

That outputs something like this: `Fri Sep 18 12:52:33 -0700 2015`

Try as I did, I could not prepend "Last login: " and append " from <ip>" to it and have it show on one line. My bash-fu is too weak. Hopefully someone else's is stronger and can take that to completion.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-03-16 22:24](https://github.com/Russell91/sshrc/issues/53#issuecomment-197584124):

I'm going to archive this issue for now.


-------------------------------------------------------------------------------

# [\#50 Issue](https://github.com/Russell91/sshrc/issues/50) `open`: Add homebrew bash completion
**Labels**: `enhancement`


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2015-08-26 19:59](https://github.com/Russell91/sshrc/issues/50):

Continuation of https://github.com/Russell91/sshrc/issues/44#issuecomment-124967391. Request for comment on the best way to add bash completion on homebrew for OSX.

See http://www.harding.motd.ca/autossh/ for an example of another tool that has reasonable completion.


#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-26 22:52](https://github.com/Russell91/sshrc/issues/50#issuecomment-135199350):

@Russell91 , what do you think about https://github.com/Homebrew/homebrew-completions ?

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-26 23:18](https://github.com/Russell91/sshrc/issues/50#issuecomment-135203485):

See https://github.com/Russell91/sshrc/issues/49#issuecomment-135203140

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-29 20:58](https://github.com/Russell91/sshrc/issues/50#issuecomment-136050201):

@evverx seems reasonable. What are the alternatives?

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-31 13:56](https://github.com/Russell91/sshrc/issues/50#issuecomment-136378481):

@Russell91 , `bash_completion.install` in the [`sshrc`](https://github.com/Homebrew/homebrew/blob/master/Library/Formula/sshrc.rb) formula.
See [`git.rb`](https://github.com/Homebrew/homebrew/blob/master/Library/Formula/git.rb#L117).


-------------------------------------------------------------------------------

# [\#49 Issue](https://github.com/Russell91/sshrc/issues/49) `open`: Add apt-get bash completion
**Labels**: `enhancement`


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2015-08-26 19:57](https://github.com/Russell91/sshrc/issues/49):

Continuation of https://github.com/Russell91/sshrc/issues/44#issuecomment-124967391. Request for comment on the best way to add bash completion on apt-get for Ubuntu 12.04+.

See http://www.harding.motd.ca/autossh/ for an example of another tool that has reasonable completion.


#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-26 22:48](https://github.com/Russell91/sshrc/issues/49#issuecomment-135198778):

@Russell91 , you can:
- Add `Build-Depends: debhelper` to `debian/control` (`Source: sshrc` section)
- Add `Build-Depends-Indep: bash-completion` to `debian/control` (`Source: sshrc` section)
- Add `Recommends: bash-completion` to `debian/control` (`Package: sshrc` section)
- Add

``` make
override_dh_auto_install:
    dh_auto_install
    dh_bash-completion
```

to `debian/rules`
- Create `debian/sshrc.bash-completion`

``` sh
_completion_loader ssh 2>/dev/null # for bash-completion >= 1.90, bash >= 4.1
eval $(complete -p ssh | sed 's/ ssh$/ sshrc/')
```

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-26 23:16](https://github.com/Russell91/sshrc/issues/49#issuecomment-135203140):

Well, the simplest way: update `bash-completion`:)
See:
- [add autossh to list of commands that perform _ssh() completion](http://anonscm.debian.org/cgit/bash-completion/bash-completion.git/commit/?id=d2a7c9cd784ae2354e8337368cf)
- [Do rest of splits, add symlinking for files defining multiple completions.](http://anonscm.debian.org/cgit/bash-completion/bash-completion.git/commit/?id=efad9540e531bd3f662a9)

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-26 23:50](https://github.com/Russell91/sshrc/issues/49#issuecomment-135207402):

Is it safe to post my debian folder on the apt-get branch? That would probably make it much easier for people to suggest these sort of changes.

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-27 00:18](https://github.com/Russell91/sshrc/issues/49#issuecomment-135215389):

> Is it safe to post my debian folder on the apt-get branch?

Yes, it's safe.

> That would probably make it much easier for people to suggest these sort of changes.

Ok.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-27 00:27](https://github.com/Russell91/sshrc/issues/49#issuecomment-135216513):

I just pushed the debian folder to the apt-get.

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-27 00:56](https://github.com/Russell91/sshrc/issues/49#issuecomment-135222508):

@Russell91 , done

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-27 01:33](https://github.com/Russell91/sshrc/issues/49#issuecomment-135236125):

But [dh_bash-completion still installs files in /etc/bash_completion](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=668254)
Fixed in `2.1-4.2`

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-08-27 01:53](https://github.com/Russell91/sshrc/issues/49#issuecomment-135238668):

I've removed `dh_bash-completion`.
Used an `install` mechanism instead.


-------------------------------------------------------------------------------

# [\#48 Issue](https://github.com/Russell91/sshrc/issues/48) `open`: man page
**Labels**: `enhancement`


#### <img src="https://avatars2.githubusercontent.com/u/1759876?v=3" width="50">[Pranav Kant](https://github.com/pranavk) opened issue at [2015-08-26 19:14](https://github.com/Russell91/sshrc/issues/48):

would be great if we have a man page.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-26 20:06](https://github.com/Russell91/sshrc/issues/48#issuecomment-135156137):

Good idea. We're trying out a new strategy where features like this would be bundled into installations for either homebrew or apt-get (or something else?), although it seems like standardizing the man page across these installs would be a good idea. What's the best way to add a man page to an e.g. apt-get installed tool?

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-26 20:11](https://github.com/Russell91/sshrc/issues/48#issuecomment-135157117):

@pranavk 
Also, it seems based on https://bugzilla.redhat.com/show_bug.cgi?id=1247328#c1 that you have some interest in setting up Fedora support. I've created a Fedora branch as well. I'd like to modify the master readme to suggest the simple install, or to link to the ubuntu, osx, fedora, and archlinux pages for installation. Those pages could then have 1-2 paragraph set of install instructions on their respective system.

#### <img src="https://avatars2.githubusercontent.com/u/1759876?v=3" width="50">[Pranav Kant](https://github.com/pranavk) commented at [2015-09-27 07:57](https://github.com/Russell91/sshrc/issues/48#issuecomment-143527995):

Sorry for such a late reply.

> What's the best way to add a man page to an e.g. apt-get installed tool?

The best way would have been using autotools, and let it install the man pages for you[1]. But since this package is not very big, I don't using autotools is worth it.
What we can do is simply write the man pages using manedit[2], or something similar and include those man pages in the source tree (preferably under a man subdirectory). The package maintainers from various distributions can then pick them up and install them appropriately.

[1] http://www.gnu.org/software/automake/manual/html_node/Man-Pages.html
[2] http://freecode.com/projects/manedit

#### <img src="https://avatars2.githubusercontent.com/u/1759876?v=3" width="50">[Pranav Kant](https://github.com/pranavk) commented at [2015-10-08 17:22](https://github.com/Russell91/sshrc/issues/48#issuecomment-146629850):

jfyi, that we are on fedora now.

as of now, i didn't include any man pages in the release.


-------------------------------------------------------------------------------

# [\#47 Issue](https://github.com/Russell91/sshrc/issues/47) `closed`: proper quoting required

#### <img src="https://avatars2.githubusercontent.com/u/1759876?v=3" width="50">[Pranav Kant](https://github.com/pranavk) opened issue at [2015-08-10 07:42](https://github.com/Russell91/sshrc/issues/47):

Would be great if we fix it upstream here, rather than having a patch downstream[1].

```
 if [ $1 ]; then
      command -v xxd >/dev/null 2>&1 || { echo >&2 "sshrc requires xxd to be installed locally, but it's not. Aborting."; exit 1; }
      sshrc $@
```

This is an accident waiting to happen. Proper quoting is required around $@. [ $1 ] will go wrong if options are given on the command line."

[1] https://bugzilla.redhat.com/show_bug.cgi?id=1247328#c1


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-26 19:42](https://github.com/Russell91/sshrc/issues/47#issuecomment-135149764):

We'll get this fixed. Are there any other shell idioms that are being violated?

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-26 20:22](https://github.com/Russell91/sshrc/issues/47#issuecomment-135159627):

fixed by https://github.com/Russell91/sshrc/commit/3d507b15026920eebd8388b4fd55a31a3135542e


-------------------------------------------------------------------------------

# [\#45 Issue](https://github.com/Russell91/sshrc/issues/45) `closed`: `deb`-package is outdated

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) opened issue at [2015-07-26 19:50](https://github.com/Russell91/sshrc/issues/45):

Hi, @Russell91 !
Thanks for the useful tool!

There are two problems with `deb`-package:
- `0.4` is outdated:

```
apt-get download sshrc
# Get:1 http://ppa.launchpad.net/russell-s-stewart/ppa/ubuntu/ vivid/main sshrc all 0.4-trusty-1 [2,726 B]
dpkg-deb --raw-extract sshrc_0.4-trusty-1_all.deb SSHRC
cd SSHRC/usr/bin
wget https://raw.githubusercontent.com/Russell91/sshrc/master/sshrc -O last
diff -q sshrc last
# Files sshrc and last differ
```
- Missing `vim-common` (for `xxd`) in the `debian/control`'s `Depends` field. 


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-07-26 23:01](https://github.com/Russell91/sshrc/issues/45#issuecomment-125046953):

Good idea about adding vim-common to the dependency list. Just took care of that and updated the repository.

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-07-27 09:31](https://github.com/Russell91/sshrc/issues/45#issuecomment-125145208):

@Russell91 , thanks. Works fine :+1:


-------------------------------------------------------------------------------

# [\#44 Issue](https://github.com/Russell91/sshrc/issues/44) `closed`: missing bash completion

#### <img src="https://avatars0.githubusercontent.com/u/4653434?v=3" width="50">[Julian](https://github.com/nightvisi0n) opened issue at [2015-07-19 16:09](https://github.com/Russell91/sshrc/issues/44):

It would be very fine if we have the same bash completion features as in ssh (host completion based on ssh's config, known hosts, etc.).
Otherwise it is hard to archive the same productivity as with native ssh.

There where two pull requests based on this feature request (#11 , #25).
#11 is already closed, but #25 is still open and needs some help!


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-07-19 19:04](https://github.com/Russell91/sshrc/issues/44#issuecomment-122695666):

Okay, I think it was mostly my fault that people stopped working on this. But I still want to ensure we hit a certain quality before we can merge. In particular, my two big requirements are that

a) It works on both Ubuntu and OS X (even if there is special casing)
b) It requires the user to at most add a single line to their .bashrc

(b) is the tough one because many users install sshrc by simply downloading the file. Thus, it will require some creativity to avoid people downloading multiple files. The reason (b) is important though is because in my mind the cost of 5 minutes of up front configuration outweighs the value of the feature for most users.

Perhaps one could add the bash completion logic to the sshrc file and the user could add "source `which sshrc`" to their .bashrc? We'd need to make sure sshrc was designed be sourced in that case. If anyone has good ideas here that would be nice as well.

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-07-26 10:26](https://github.com/Russell91/sshrc/issues/44#issuecomment-124967391):

@jneureuther ,
- install [`bash-completion`](http://bash-completion.alioth.debian.org/)
- Add the following lines to your `~/.bashrc` (`~/.bash_profile` on OSX)

``` bash
_completion_loader ssh 2>/dev/null # for bash-completion >= 1.90, bash >= 4.1
eval $(complete -p ssh | sed 's/ ssh$/ sshrc/')
```

See also: http://unix.stackexchange.com/a/216899/120177

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-08-26 19:59](https://github.com/Russell91/sshrc/issues/44#issuecomment-135154610):

This works great, and it is more robust than anything I've put together, but the install is way above the level of difficulty that would make sense to put on the readme. Instead, I'm opening up two new branches on sshrc, apt-get and homebrew, that will allow us to tailor features like this to specific installs. Both package managers will make it easy to hide this complexity in a more traditional install mechanism. This will create two types of sshrc - one that is fully featured and comes with package managers, and one that is a lightweight single bash file that can be installed anywhere. See either https://github.com/Russell91/sshrc/issues/49 or https://github.com/Russell91/sshrc/issues/50

#### <img src="https://avatars2.githubusercontent.com/u/4771462?v=3" width="50">[disrupted](https://github.com/disrupted) commented at [2017-05-05 18:24](https://github.com/Russell91/sshrc/issues/44#issuecomment-299539954):

is there any way to get completion with this method using ZSH instead of Bash?


-------------------------------------------------------------------------------

# [\#42 Issue](https://github.com/Russell91/sshrc/issues/42) `closed`: Wrong bash version on OS X server is being used

#### <img src="https://avatars0.githubusercontent.com/u/4442114?v=3" width="50">[Matthew Chen](https://github.com/mchenja) opened issue at [2015-06-14 18:43](https://github.com/Russell91/sshrc/issues/42):

When I use regular `ssh`:

```
[mchenja@mycomp ~]$ ssh remotecomp.mydomain.com
remotecomp:~ mchenja$ echo $BASH_VERSION
4.3.33(1)-release
```

When I use `sshrc`:

```
[mchenja@mycomp ~]$ sshrc remotecomp.mydomain.com
[mchenja@remotecomp ~]$ echo $BASH_VERSION
3.2.57(1)-release
```

I installed bash 4 on my remote computer using homebrew, if you think that might affect the issue.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-06-14 21:27](https://github.com/Russell91/sshrc/issues/42#issuecomment-111877081):

Yea, I don't know what your exact setup is, but it looks like your path may be favoring the older version of bash. Maybe you could try swapping out `bash` in line 33 of https://github.com/Russell91/sshrc/blob/master/sshrc: 
`exec bash --rcfile <(echo '`

for the full path to your preferred bash executable?

#### <img src="https://avatars0.githubusercontent.com/u/4442114?v=3" width="50">[Matthew Chen](https://github.com/mchenja) commented at [2015-06-15 01:26](https://github.com/Russell91/sshrc/issues/42#issuecomment-111895857):

I haven't tried that yet, but I made my (local) `.sshrc` file an empty file, and I also deleted my `.bashrc` and `.bash_profile` files on my remote computer to help debug the issue.

Here's what I see when I use regular `ssh`:

```
[mchenja@mycomp ~]$ ssh remotecomp.mydomain.com
remotecomp:~ mchenja$ echo $BASH_VERSION
4.3.33(1)-release
remotecomp:~ mchenja$ which bash
/usr/local/bin/bash
remotecomp:~ mchenja$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Applications/Server.app/Contents/ServerRoot/usr/bin:/Applications/Server.app/Contents/ServerRoot/usr/sbin
```

But when I use `sshrc`, here's what happens:

```
[mchenja@mycomp ~]$ sshrc remotecomp.mydomain.com
bash-3.2$ echo $BASH_VERSION
3.2.57(1)-release
bash-3.2$ which bash
/bin/bash
bash-3.2$ echo $PATH
/usr/bin:/bin:/usr/sbin:/sbin:/var/folders/m7/2lsx99rn2x109gmchxn2sp_r0000gn/T/.mchenja.sshrc.XXXX.INeVA8xH
```

Clearly, some code in `sshrc` is changing my path, and perhaps not loading some (system-generated) `.bashrc` file somewhere which adds the `/usr/local/bin` path (for `brew`) as well as the `Server.app` paths.

For what it's worth, I don't think this is an idiosyncratic issue. I'd suspect that anyone who has homebrew installed on their remote computer should have a similar issue.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-07-03 20:49](https://github.com/Russell91/sshrc/issues/42#issuecomment-118423358):

Can you confirm whether you were able to get things working with the fix? At this point, the root cause is that sshrc does not fully support the remote server being OS X, simply because I don't have any OS X server's to ssh into and test on. If you have figured out a cleaner way to fix the problem than the hack I suggested, please consider submitting a pull request or just letting me know.

#### <img src="https://avatars0.githubusercontent.com/u/4442114?v=3" width="50">[Matthew Chen](https://github.com/mchenja) commented at [2015-07-09 00:26](https://github.com/Russell91/sshrc/issues/42#issuecomment-119769371):

Actually solving the problem has proven to be a bit trickier than I expected, since I'm not very familiar with some of the functions called in your code. But I have a good understanding of the issues, so I'll explain them here, and I submitted pull request #43 to fix the first one.

#### Issue 1: Incorrect Path on Mac OS X

Looking at the man page for `bash` on Mac OS X, it explains:

_When bash is invoked as an interactive login shell, it first reads and executes commands from the file `/etc/profile`, if that file exists. After reading that file, it looks for `~/.bash_profile`, `~/.bash_login`, and `~/.profile`, in that order, and reads and executes commands from the first one that exists and is readable._

The man pages for `bash` on `corn.stanford.edu` and `myth.stanford.edu`, both of which are running Ubuntu, specify the same behavior.

Currently, `sshrc` doesn't read these files that are specified by the man page, so I wrote code to do so, tested on my Mac and two linux machines and submitted pull request #43.

#### Issue 2: Wrong Bash Version on Mac OS X

The issue is that the shell spawned by `ssh <various commands>` is the default version of `bash`, even after the user has changed shells with `chsh -s`. For example:

_ssh without any commands_

```
[mchenja@mycomp ~]$ ssh localhost
[mchenja@mycomp ~]$ echo $BASH
/usr/local/bin/bash
```

_ssh with commands_

```
[mchenja@mycomp ~]$ ssh localhost 'echo $BASH'
/bin/bash
```

##### Possible Fix

As long as the correct path is present, calling `exec bash` should load the desired `bash`. For example:

```
[mchenja@mycomp ~]$ ssh localhost 'source /etc/profile; exec bash'
echo $BASH
/usr/local/bin/bash
```

However, I've been unable to merge this fix into `sshrc`; I also tried your suggested fix, but it didn't work:

_before the change_

```
[mchenja@mycomp sshrc]$ sed -n '33p' sshrc
exec bash --rcfile <(echo '
[mchenja@mycomp sshrc]$ ./sshrc localhost
[mchenja@mycomp ~]$ echo $BASH
/bin/bash
```

_after the change_

```
[mchenja@mycomp sshrc]$ sed -n '33p' sshrc
exec /usr/local/bin/bash --rcfile <(echo '
[mchenja@mycomp sshrc]$ ./sshrc localhost
[mchenja@mycomp ~]$ echo $BASH
/bin/bash
```

Consequently, I think there must be some other aspect of your code that is affecting which `bash` is executed, but I'm unsure what that aspect is.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-07-12 05:33](https://github.com/Russell91/sshrc/issues/42#issuecomment-120689389):

Merged into master.


-------------------------------------------------------------------------------

# [\#41 Issue](https://github.com/Russell91/sshrc/issues/41) `closed`: SSHHOME is incorrect (deleted) when resuming Tmux sessions

#### <img src="https://avatars0.githubusercontent.com/u/43789?v=3" width="50">[Matthew O'Riordan](https://github.com/mattheworiordan) opened issue at [2015-06-08 09:29](https://github.com/Russell91/sshrc/issues/41):

I find that upon SSHRC'ing back into a box a second time with a Tmux session left running, the variable $SSHHOME is invalid because the folder has been deleted.

Probably easiest to explain with a log:

```
# first time to connect to the server
$ sshrc my-remote-server.com

remote $ tmux -S /tmp/matt.tmuxserver

remote $ echo $SSHHOME
/tmp/.mattheworiordan.sshrc.fZxN

# check to see if the folder & contents exist
remote $ ls $SSHHOME
bashsshrc  sshrc  sshrc.bashrc

# Detach from tmux
Ctrl-B, Ctrl-D

# second connect to the server
$ sshrc my-remote-server.com

# Checking SSHHOME confirms a new folder has been created
remote $ echo $SSHHOME
/tmp/.mattheworiordan.sshrc.GD0

# Attach to the Tmux session
remote $ tmux -S /tmp/matt.tmuxserver

# SSHHOME still points to the old folder
remote $ echo $SSHHOME
/tmp/.mattheworiordan.sshrc.fZxN

# Unfortunately SSHHOME does not exist
remote $ ls $SSHHOME
ls: cannot access /tmp/.mattheworiordan.sshrc.fZxN: No such file or directory
```

What do you recommend to get around this problem?


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-06-11 18:41](https://github.com/Russell91/sshrc/issues/41#issuecomment-111235665):

Yea, this problem requires some clever tricks to avoid. But fortunately, they are already in the readme! If you consult the provided tmuxrc function:

```
tmuxrc ()
{
    local TMUXDIR=/tmp/russelltmuxserver;
    if ! [ -d $TMUXDIR ]; then
        rm -rf $TMUXDIR;
        mkdir -p $TMUXDIR;
    fi;
    rm -rf $TMUXDIR/.sshrc.d;
    cp -r $SSHHOME/.sshrc $SSHHOME/bashsshrc $SSHHOME/sshrc $SSHHOME/.sshrc.d $TMUXDIR;
    SSHHOME=$TMUXDIR SHELL=$TMUXDIR/bashsshrc /usr/bin/tmux -S $TMUXDIR/tmuxserver $@
}
```

You will notice that it takes a step to copy the contents of your old $SSHHOME into a special tmux directory that will not be deleted when your original shell exits. Of course, you'll have to modify the TMUXDIR to be your own `/tmp/mattheworiordantmuxserver`, but otherwise you should be good to go.

#### <img src="https://avatars0.githubusercontent.com/u/43789?v=3" width="50">[Matthew O'Riordan](https://github.com/mattheworiordan) commented at [2015-06-12 17:45](https://github.com/Russell91/sshrc/issues/41#issuecomment-111571419):

Thanks @Russell91, you're a legend.  I had misinterpreted your example, but I understand it now and have it all working as expected.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-06-14 21:20](https://github.com/Russell91/sshrc/issues/41#issuecomment-111876766):

Okay, is there any way that the Readme example could have been more clear?

#### <img src="https://avatars0.githubusercontent.com/u/43789?v=3" width="50">[Matthew O'Riordan](https://github.com/mattheworiordan) commented at [2015-06-17 10:23](https://github.com/Russell91/sshrc/issues/41#issuecomment-112746802):

@Russell91 I think it was my fault because I tried to modify it for my needs.  The only thing I did find odd is that in your example you execute Tmux as follows:

```
SSHHOME=$TMUXDIR SHELL=$TMUXDIR/bashsshrc /usr/bin/tmux -S $TMUXDIR/tmuxserver $@
```

However, the `bashsshrc` file, at least in my environment, simply loads `.sshrc` so it loads itself?


-------------------------------------------------------------------------------

# [\#40 Issue](https://github.com/Russell91/sshrc/issues/40) `closed`: Agent forwarding support?

#### <img src="https://avatars3.githubusercontent.com/u/5847?v=3" width="50">[Scott Rubin](https://github.com/Apreche) opened issue at [2015-04-05 22:12](https://github.com/Russell91/sshrc/issues/40):

Let's say I use agent forwarding to SSH from machine A to machine B, then from machine B to machine C. I've only configured my vimrc and such on machine A, which is the machine I am physically sitting at. Will the vimrc end up all the way on machine B?


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-04-05 22:22](https://github.com/Russell91/sshrc/issues/40#issuecomment-89864885):

I'm not sure how you are accomplishing "agent forwarding", but my suspicion is that it will not work. However, sshrc does copy it's own binary to machine B, so you can do `sshrc B` followed by `sshrc C`, and the vimrc will end up all the way on machine C. To make this more convenient, you can add to your sshrc a line that says:

```
if [ `hostname | grep B | wc -l` == 1 ]; then
    sshrc C
fi
```

That's how I've done it in this case at least.


-------------------------------------------------------------------------------

# [\#39 Issue](https://github.com/Russell91/sshrc/issues/39) `closed`: Homebrew support

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2015-04-05 21:27](https://github.com/Russell91/sshrc/issues/39):

If someone could create a homebrew recipe, I can link to it on the readme. There was a problem early on with sshrc where the homebrew recipe fell out of date and was causing problems for users, but things are much more stable now and I think it would be nice for mac users to have this option.





-------------------------------------------------------------------------------

# [\#37 Issue](https://github.com/Russell91/sshrc/issues/37) `closed`: Freebsd support

#### <img src="https://avatars1.githubusercontent.com/u/622187?v=3" width="50">[Moddus](https://github.com/Moddus) opened issue at [2014-11-04 21:59](https://github.com/Russell91/sshrc/issues/37):

Hi,
thanks for your work. Are you planning to make sshrc available on freebsd ?
I'm get following output but I'm not able to fix it :(

```
Ambiguous output redirect.
if: Expression Syntax.
then: Command not found.
fi: Command not found.
Illegal variable name.
SSHHOME: Undefined variable.
SSHRCCLEANUP: Undefined variable.
Illegal variable name.
SSHHOME: Undefined variable.
Illegal variable name.
Illegal variable name.
SSHHOME: Undefined variable.
Illegal variable name.
SSHHOME: Undefined variable.
SSHHOME: Undefined variable.
Connection to xxx.xxxx.xxxx.xxxx closed.
```

Regards,
Moddus


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-03-21 08:51](https://github.com/Russell91/sshrc/issues/37#issuecomment-84283154):

I don't have a freebsd system, so I can't offer much assistence. I'm still hoping another user would come along and be able to assist you.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-04-16 01:04](https://github.com/Russell91/sshrc/issues/37#issuecomment-93609578):

Can you tell me the output of `bash --version`? Mine is 3.2.51 and works.

#### <img src="https://avatars2.githubusercontent.com/u/14026947?v=3" width="50">[nandeska](https://github.com/nandeska) commented at [2016-03-18 18:33](https://github.com/Russell91/sshrc/issues/37#issuecomment-198487887):

I confirm that behavior with my FreeBSD servers. FreeBSD handles redirects and shells variables in a different way than Linux, I'm checking how sshrc could work with it


-------------------------------------------------------------------------------

# [\#36 Issue](https://github.com/Russell91/sshrc/issues/36) `open`: Screen support?
**Labels**: `enhancement`


#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) opened issue at [2014-10-15 09:52](https://github.com/Russell91/sshrc/issues/36):

Has anyone made this work with `screen`?
`tmux` may not be available on the target machine, `screen` is more often.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-10-15 09:56](https://github.com/Russell91/sshrc/issues/36#issuecomment-59182884):

You can certainly try. I'll give you a slot on the wiki if you design a
screenrc function that works the same as tmuxrc. You'll need to look
through different environment variables, and there are often lots of corner
cases. Good luck if you look into it. I don't use screen so it's not at the
top of my list.

On Wed, Oct 15, 2014 at 2:52 AM, Thomas Riccardi notifications@github.com
wrote:

> Has anyone made this work with screen?
> tmux may not be available on the target machine, screen is more often.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/36.

#### <img src="https://avatars0.githubusercontent.com/u/325377?v=3" width="50">[Frank Hoffsümmer](https://github.com/captnswing) commented at [2015-11-05 09:50](https://github.com/Russell91/sshrc/issues/36#issuecomment-154009504):

I had a first quick stab at doing this

```
screenrc() {
    local SCREENDIR=/tmp/russellscreenserver
    if ! [ -d $SCREENDIR ]; then
        rm -rf $SCREENDIR
        mkdir -p $SCREENDIR
    fi
    rm -rf $SCREENDIR/.sshrc.d
    cp -r $SSHHOME/.sshrc $SSHHOME/bashsshrc $SSHHOME/sshrc $SSHHOME/.sshrc.d $SCREENDIR
    SSHHOME=$SCREENDIR /usr/bin/screen -c $SCREENDIR/.sshrc.d/.screenrc -s $SCREENDIR/bashsshrc $@
}
```

not completely good yet, works only for all subsequently opened screens (C-a), not the first one

#### <img src="https://avatars2.githubusercontent.com/u/5619681?v=3" width="50">[cryptid11](https://github.com/cryptid11) commented at [2017-02-08 01:26](https://github.com/Russell91/sshrc/issues/36#issuecomment-278200543):

any news on this? do I have to start using tmux? XD


-------------------------------------------------------------------------------

# [\#35 Issue](https://github.com/Russell91/sshrc/issues/35) `closed`: Duplicate `rm -rf \$SSHRCCLEANUP`

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) opened issue at [2014-09-30 18:04](https://github.com/Russell91/sshrc/issues/35):

A trap is setup at exit to cleanup the temporary directory.
But in case of non error exit, a second `rm -rf \$SSHRCCLEANUP`  is also executed after `\$SSHHOME/bashsshrc`. It should probably be removed.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-30 20:22](https://github.com/Russell91/sshrc/issues/35#issuecomment-57376482):

yea, I'm not sure what the semantics of trap '...' 0 are. Does this get called in every case, or just when there is an error thrown? rm -rf needs to be called in every case.

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-09-30 20:36](https://github.com/Russell91/sshrc/issues/35#issuecomment-57378527):

From the GNU bash manual:

```
trap [-lp] [arg] [sigspec …]
...
If a sigspec is 0 or EXIT, arg is executed when the shell exits.
```

I've never seen any trap duplicated like this, so it should work with just the trap. Plus it's easy to test.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-30 20:47](https://github.com/Russell91/sshrc/issues/35#issuecomment-57380152):

Perfect, that's exactly what I needed to know. I tested and it worked
without the duplicated, but I put it in there just in case.

On Tue, Sep 30, 2014 at 1:36 PM, Thomas Riccardi notifications@github.com
wrote:

> From the GNU bash manual:
> 
> trap [-lp] [arg] [sigspec …]
> ...
> If a sigspec is 0 or EXIT, arg is executed when the shell exits.
> 
> I've never seen any trap duplicated like this, so it should work with just
> the trap. Plus it's easy to test.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/35#issuecomment-57378527.


-------------------------------------------------------------------------------

# [\#34 Issue](https://github.com/Russell91/sshrc/issues/34) `closed`: sshrc example.com "ls" doesn't exit after executing "ls"

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) opened issue at [2014-09-29 12:56](https://github.com/Russell91/sshrc/issues/34):

With plain ssh `ssh example.com "ls"` executes the command then exits. With sshrc it doesn't exit: the interactive shell is kept open.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-29 17:00](https://github.com/Russell91/sshrc/issues/34#issuecomment-57192388):

To fix this we'd have to start parsing the sshrc arguments and act differently when extra arguments are supplied. Is there some reason why you can't just use regular ssh in these cases? I can imagine this would be frustrating if you had put alias ssh=sshrc somewhere.

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-09-29 20:02](https://github.com/Russell91/sshrc/issues/34#issuecomment-57220022):

I don't have a real use-case that would justify this.
However I would have expected sshrc could be a drop-in replacement as suggested by your alias ssh=sshrc.

In fact I do have a real use-case (but it does not necessarily justify the fix): I came across this issue while benchmarking the overhead with a `time sshrc example.com l` (where `alias l='ls -latrh'`).

In any case, if we want to have the perfect drop-in replacement there is probably more work to do. For example pipe into sshrc seem to work but triggers a warning:

```
$ echo test | sshrc example.com cat
Pseudo-terminal will not be allocated because stdin is not a terminal.
test
```

Maybe it doesn't work with older ssh/bash though this should be in another issue...

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2015-03-21 08:52](https://github.com/Russell91/sshrc/issues/34#issuecomment-84283182):

I'm closing this because it's not a bug. I'll keep in mind the fact that the current readme does not do a good job at highlighting some of the more subtle differences between sshrc and ssh though.


-------------------------------------------------------------------------------

# [\#32 Issue](https://github.com/Russell91/sshrc/issues/32) `closed`: Does sshrc work with mosh?
**Labels**: `help wanted`


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2014-09-26 05:07](https://github.com/Russell91/sshrc/issues/32):

I don't use mosh. Can someone who does try to make sshrc work with it and add a wiki page. There seems to be a good deal of demand here.





-------------------------------------------------------------------------------

# [\#29 Issue](https://github.com/Russell91/sshrc/issues/29) `closed`: It doesn't let me change the prompt colours

#### <img src="https://avatars2.githubusercontent.com/u/2475920?v=3" width="50">[Poyeyo](https://github.com/Poyeyo) opened issue at [2014-09-25 20:13](https://github.com/Russell91/sshrc/issues/29):

I just tried adding this to the config file:

PS1='${debian_chroot:+($debian_chroot)}[\033[01;32m]\u@\h[\033[00m]:[\033[01;34m]\w[\033[00m]\$ '


#### <img src="https://avatars3.githubusercontent.com/u/3211560?v=3" width="50">[robled](https://github.com/robled) commented at [2014-09-25 20:24](https://github.com/Russell91/sshrc/issues/29#issuecomment-56878158):

Strange.  Works fine for me.  Example here:

https://github.com/robled/dotfiles-core/blob/master/.sshrc

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-25 20:49](https://github.com/Russell91/sshrc/issues/29#issuecomment-56881690):

Yep, works for me too. I use the following:
    export PS1='[\033[01;32m]\u@\h[\033[00m]:[\033[01;34m]\w[\033[00m]\$ '


-------------------------------------------------------------------------------

# [\#27 Issue](https://github.com/Russell91/sshrc/issues/27) `closed`: example vim config not compatible with "syn on"

#### <img src="https://avatars3.githubusercontent.com/u/3211560?v=3" width="50">[robled](https://github.com/robled) opened issue at [2014-09-25 18:43](https://github.com/Russell91/sshrc/issues/27):

```
$ vim
Error detected while processing /tmp/.user.sshrc.OsBK/.sshrc.d/vimrc:
line    1:
E484: Can't open file /tmp/.user.sshrc.OsBK/.sshrc.d/syntax/syntax.vim
Press ENTER or type command to continue
```

A user on reddit posted a solution that works for me:

https://www.reddit.com/r/linux/comments/2h0wab/sshrc_make_your_ssh_sessions_feel_like_home/ckomxkk

I will update the docs and submit a pull request shortly.


#### <img src="https://avatars3.githubusercontent.com/u/3211560?v=3" width="50">[robled](https://github.com/robled) commented at [2014-09-25 21:13](https://github.com/Russell91/sshrc/issues/27#issuecomment-56884895):

Closing this out since the fix was merged:

https://github.com/Russell91/sshrc/pull/28

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-25 21:19](https://github.com/Russell91/sshrc/issues/27#issuecomment-56885799):

Yea, thanks for submitting this. I was just about to start working on this after fixing the tmux issues last night, when I saw this solution sitting here ready for me to add.


-------------------------------------------------------------------------------

# [\#26 Issue](https://github.com/Russell91/sshrc/issues/26) `closed`: mktemp on Ubuntu 6.06 doesn't accept a parameter to -t

#### <img src="https://avatars0.githubusercontent.com/u/1532071?v=3" width="50">[Evgeni Kolev](https://github.com/edkolev) opened issue at [2014-09-25 08:29](https://github.com/Russell91/sshrc/issues/26):

Thanks for this amazing script!

Here's an issue I ran into: when connecting to a linux box from OSX, I get an error:
`mktemp: cannot make temp dir /tmp/.edkolev.sshrc.XXXX: Invalid argument`

I believe this is caused by the fact the mktemp's command line API is different:

```
(man mktemp on linux; -t is a switch)
SYNOPSIS
       mktemp [-V] | [-dqtu] [-p directory] [template]
```

```
(man mktemp on osx; -t accepts a param)

SYNOPSIS
     mktemp [-d] [-q] [-t prefix] [-u] template ...
     mktemp [-d] [-q] [-u] -t prefix
```


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-25 08:45](https://github.com/Russell91/sshrc/issues/26#issuecomment-56790272):

damn, I was under the impression that mktemp -d -t ... was consistent with every version of mktemp. Can you send me the man page for mktemp on your system?

#### <img src="https://avatars0.githubusercontent.com/u/1532071?v=3" width="50">[Evgeni Kolev](https://github.com/edkolev) commented at [2014-09-25 09:12](https://github.com/Russell91/sshrc/issues/26#issuecomment-56793063):

`-p directory` I think. Here's the whole man page. BTW this is a very old Ubuntu 6.06.1 LTS, I don't have a newer one to test right now

https://gist.github.com/edkolev/fb816c804d67d1c83b8e

#### <img src="https://avatars0.githubusercontent.com/u/1532071?v=3" width="50">[Evgeni Kolev](https://github.com/edkolev) commented at [2014-09-25 09:14](https://github.com/Russell91/sshrc/issues/26#issuecomment-56793279):

Actually, I do have a newer Ubuntu 14.04 LTS. Here's its man page:

https://gist.github.com/edkolev/6ff2263c25ee4e637e28

Edit: on this newer Ubuntu, sshrc is working perfectly fine. Maybe it's not really worth it to try to make sshrc work on the archaic Ubuntu

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-25 19:48](https://github.com/Russell91/sshrc/issues/26#issuecomment-56873304):

Well thanks for letting me know. I really need a better way to predict when certain commands will fail. I'm going to mark this as closed for now.


-------------------------------------------------------------------------------

# [\#25 PR](https://github.com/Russell91/sshrc/pull/25) `open`: Add Bash completion script

#### <img src="https://avatars3.githubusercontent.com/u/1656361?v=3" width="50">[Mario del Pozo](https://github.com/mariodpros) opened issue at [2014-09-24 20:05](https://github.com/Russell91/sshrc/pull/25):

Enables the same nice Bash completion features as in ssh (host completion based on ssh's config, known hosts, etc.).


#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-09-29 12:54](https://github.com/Russell91/sshrc/pull/25#issuecomment-57155825):

It doesn't work on ubuntu 12.04 with bash 4.2: `_xfunc: command not found`.

#### <img src="https://avatars3.githubusercontent.com/u/1656361?v=3" width="50">[Mario del Pozo](https://github.com/mariodpros) commented at [2014-09-29 17:47](https://github.com/Russell91/sshrc/pull/25#issuecomment-57199875):

@Niluge-KiWi Yes, you're right. I tested with an old precise laptop and the Bash completion mechanism is different.

#### <img src="https://avatars3.githubusercontent.com/u/1656361?v=3" width="50">[Mario del Pozo](https://github.com/mariodpros) commented at [2014-09-29 20:58](https://github.com/Russell91/sshrc/pull/25#issuecomment-57228786):

I don't think is a good idea.

If neither of both functions are available you just won't have completion for sshrc. But printing an error message each time the shell is executed... I'm pretty sure users will like it a lot ;-)

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-09-30 13:19](https://github.com/Russell91/sshrc/pull/25#issuecomment-57311847):

I confirm this new version of the PR works for me now.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-30 20:55](https://github.com/Russell91/sshrc/pull/25#issuecomment-57381312):

so you guys have made some good progress. I've noticed that `complete -p | grep ssh` will return the current completion function for ssh as long as ssh has already been tab completed. What about writing a completion function that first calls tab completion on the standard ssh, then greps for the name of the completion function it is using (e.g. `_ssh`), and finally reassigns tab completion of sshrc to be that function. Something like

```
_sshrc() {
    "tab-complete call" ssh
    local command=`complete -p | sed -n '/ ssh$/p'
    $("$command"rc)
    COMP_RETURN=$(echo $command | sed -e 's/.*\(_[^ ]*\).*/\1/')
}
```

#### <img src="https://avatars3.githubusercontent.com/u/1656361?v=3" width="50">[Mario del Pozo](https://github.com/mariodpros) commented at [2014-10-03 15:25](https://github.com/Russell91/sshrc/pull/25#issuecomment-57811248):

Well, I didn't found how to load the tab completion function for an specific command unless you search for the specific completion script for that command on the filesystem.
I managed to identify two places for the completion scripts on Debian/Ubuntu (/etc/bash_completion.d and /usr/share/bash-completion/completions) but I don't know if other distributions use different locations.

It seems that _ssh() and _xfunc() are good candidates to be stable on different versions and distributions.

It could be very good if someone can light on this topic.

#### <img src="https://avatars2.githubusercontent.com/u/10195800?v=3" width="50">[Evgeny Vereshchagin](https://github.com/evverx) commented at [2015-07-26 14:42](https://github.com/Russell91/sshrc/pull/25#issuecomment-124998198):

@mariodpros , see https://github.com/Russell91/sshrc/issues/44#issuecomment-124967391


-------------------------------------------------------------------------------

# [\#23 Issue](https://github.com/Russell91/sshrc/issues/23) `closed`: Brew problems

#### <img src="https://avatars0.githubusercontent.com/u/5376762?v=3" width="50">[Santiago Blanco](https://github.com/santiblanko) opened issue at [2014-09-24 13:05](https://github.com/Russell91/sshrc/issues/23):

Error: No available formula for sshrc
Searching taps... 


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-24 17:06](https://github.com/Russell91/sshrc/issues/23#issuecomment-56704506):

I've removed the brew install from the readme. I'll add it back in the future myself.


-------------------------------------------------------------------------------

# [\#22 Issue](https://github.com/Russell91/sshrc/issues/22) `closed`: ZSH Compatibility 

#### <img src="https://avatars0.githubusercontent.com/u/943110?v=3" width="50">[Aaron Halford](https://github.com/aaronhalford) opened issue at [2014-09-23 20:18](https://github.com/Russell91/sshrc/issues/22):

 Bash is awesome, yet ZSH and other shell compatibility would be a great addition.

Thoughts?

BTW, thanks so much for this ssh tool.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 20:42](https://github.com/Russell91/sshrc/issues/22#issuecomment-56586390):

How much of this behavior could work by calling 

```
 `$ exec /bin/zsh`
```

from your ~/.sshrc? I always assumed that approach would solve the problem.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-25 09:08](https://github.com/Russell91/sshrc/issues/22#issuecomment-56792671):

I'm going to mark this as closed. Still interested to hear your thoughts though.

#### <img src="https://avatars1.githubusercontent.com/u/661220?v=3" width="50">[Elvis](https://github.com/mu3) commented at [2016-04-05 17:16](https://github.com/Russell91/sshrc/issues/22#issuecomment-205904794):

Promt won't load up with  `exec zsh`
Here's a short screenscast http://take.ms/QTJ6W

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2016-04-05 20:15](https://github.com/Russell91/sshrc/issues/22#issuecomment-205973758):

@mu3 I'm not sure what the content of the $SHELL variable is in that video. But if you add `exec /bin/zsh`, it works for me. e.g.

```
stewartr@Russells-MacBook-Air-2:~$ sshrc hr1c
homerussell%
```

#### <img src="https://avatars1.githubusercontent.com/u/661220?v=3" width="50">[Elvis](https://github.com/mu3) commented at [2016-04-06 06:24](https://github.com/Russell91/sshrc/issues/22#issuecomment-206139112):

You're right, there was a problem with `$SHELL`, also I use `exec -l $(which zsh)` now.


-------------------------------------------------------------------------------

# [\#19 Issue](https://github.com/Russell91/sshrc/issues/19) `closed`: bashsshrc as SHELL seems to cause problems with less and mc

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) opened issue at [2014-09-23 02:45](https://github.com/Russell91/sshrc/issues/19):

mc seems to hang when running with SHELL=/tmp/...bashsshrc

The subshell ends up a stopped  'T+' and there is a new pty.

```

 pts/7    S    |   \_ bash --rcfile /dev/fd/63
 pts/7    S+   |       \_ /usr/bin/mc -P /tmp/mc-mockbuild/mc.pwd.6023
 pts/1    Ss   |           \_ /bin/bash /tmp/.mockbuild.sshrc.bI7rM2/bashsshrc -rcfile .bashrc
 pts/1    T+   |               \_ /bin/bash --rcfile /dev/fd/62
```

I notice that bashsshrc doesn't work with the usually '-c' option.  Maybe it needs to implement -c.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 03:17](https://github.com/Russell91/sshrc/issues/19#issuecomment-56472272):

hmm, there is no reason that bashsshrc can't take all the normal arguments that bash does. Can you try editing bashsshrc with `vim $(which bashsshrc)` and appending `"$@"` after the parenthesis on the final line? If this works I'll add it to master.

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-23 04:34](https://github.com/Russell91/sshrc/issues/19#issuecomment-56475466):

I think it is the interactive stuff.

```
   An interactive shell is one started without non-option arguments and without the -c option whose standard input and error are both connected to terminals (as determined by isatty(3)), or one started with the -i option.  PS1 is set and $- includes i if bash is interactive, allowing a shell script or a startup file to test this state.
```

Non-interactive shells shouldn't source a .bashrc.

bashsshrc -c  echo foo  should not source the .sshrc as it is non-interactive.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 05:44](https://github.com/Russell91/sshrc/issues/19#issuecomment-56478458):

Does the current master not work for you? Bash will not actually source the
argument of --rcfile if -c is passed as well. Please let me know if master
has fixed your problems.

On Mon, Sep 22, 2014 at 9:34 PM, Ross Brattain notifications@github.com
wrote:

> I think it is the interactive stuff.
> 
>    An interactive shell is one started without non-option arguments and without the -c option whose standard input and error are both connected to terminals (as determined by isatty(3)), or one started with the -i option.  PS1 is set and $- includes i if bash is interactive, allowing a shell script or a startup file to test this state.
> 
> Non-interactive shells shouldn't source a .bashrc.
> 
> bashsshrc -c echo foo should not source the .sshrc as it is
> non-interactive.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/19#issuecomment-56475466.

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-23 06:39](https://github.com/Russell91/sshrc/issues/19#issuecomment-56481265):

once I export SHELL=$SSHHOME/bashsshrc  
midnight commander hangs.  Oh and I guess bash accepts -rcfile for some undocumented reason.

```
pts/42   S+     \_ mc
pts/45   Ss         \_ bash /tmp/.rbbratta.sshrc.Kfd2/bashsshrc -rcfile .bashrc
pts/45   T+             \_ bash --rcfile /dev/fd/62 -rcfile .bashrc
```

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 07:03](https://github.com/Russell91/sshrc/issues/19#issuecomment-56482732):

okay, I've reproduced this and setting bashsshrc `"$@"` did not fix it. Looks like updating the shell variable is just bad news. I'll update the readme with an appropriate solution.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 07:09](https://github.com/Russell91/sshrc/issues/19#issuecomment-56483144):

okay, please let me know if the current readme suggestion fixes your problem

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-23 07:50](https://github.com/Russell91/sshrc/issues/19#issuecomment-56485981):

ah, we are forking bash, when we need to exec.  It looks like midnight commander setups up a fifo with the subshell which doesn't work if we fork a new bash in bashsshrc.

This should work

```
#!/usr/bin/env bash
exec bash --rcfile <(echo '
if [ -e /etc/bash.bashrc ]; then source /etc/bash.bashrc; fi
if [ -e ~/.bashrc ]; then source ~/.bashrc; fi
source '$SSHHOME'/.sshrc;
export PATH=$PATH:'$SSHHOME' 
') "$@"
```

I also though about removing the <(echo ...) and just writing the contents to .ssshrc.d and using a static --rcfile.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 17:36](https://github.com/Russell91/sshrc/issues/19#issuecomment-56558721):

Hmm, semantically exec makes more sense here. Are there other implications of forking rather than using exec?

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 20:55](https://github.com/Russell91/sshrc/issues/19#issuecomment-56588301):

I'm going to mark this as solved.


-------------------------------------------------------------------------------

# [\#18 Issue](https://github.com/Russell91/sshrc/issues/18) `closed`: Argument list too long

#### <img src="https://avatars1.githubusercontent.com/u/76221?v=3" width="50">[Julien Lancien](https://github.com/calexicoz) opened issue at [2014-09-22 15:01](https://github.com/Russell91/sshrc/issues/18):

Whenever I try to use this script, I get the following error:

```
$ sshrc localhost
./sshrc: line 9: /usr/bin/ssh: Argument list too long
```

My `~/.sshrc.d` is pretty small:

```
$ du -hs
 16K    .
```

Though I have a bunch of files (I modified the tar command to exclude `.git`):

```
$ find -L . | grep -v .git | wc
     568     568   27240
```

Not sure what is the best way to debug this. Any idea?

Thanks!


#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 15:57](https://github.com/Russell91/sshrc/issues/18#issuecomment-56395213):

Add a -v to ssh, and add 'set -x' in the bash to enable tracing.

You might be able to increase the shell argument list size RLIMIT_STACK with ulimit -s.

#### <img src="https://avatars1.githubusercontent.com/u/76221?v=3" width="50">[Julien Lancien](https://github.com/calexicoz) commented at [2014-09-22 18:22](https://github.com/Russell91/sshrc/issues/18#issuecomment-56416703):

With `set -x` in the script, I ran this:

```
sshrc HOST 2>&1 | tee LOG
```

And the resulting log file is 15M. So it seems that 16k of files may actually be too much to represent as hexadecimal. Only other way I can think of would be to use `scp` instead of `xdd`. Maybe I'll just trim down my profile.

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 18:44](https://github.com/Russell91/sshrc/issues/18#issuecomment-56420052):

base64 instead of xdd should increase the efficiency of the encoding.  base64 is available in gnu coreutils.

#### <img src="https://avatars1.githubusercontent.com/u/76221?v=3" width="50">[Julien Lancien](https://github.com/calexicoz) commented at [2014-09-22 23:24](https://github.com/Russell91/sshrc/issues/18#issuecomment-56458552):

That reduced it a bit, to 9M, but that's still too much. I just won't use that many files. I was trying to import my `.vim` directory with all my plugins, but I can live with just my `vimrc`.

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 23:33](https://github.com/Russell91/sshrc/issues/18#issuecomment-56459342):

my testing shows a <128K limit.  I am sending the payload via the $TERM variable.  See  http://superuser.com/questions/163167/when-sshing-how-can-i-set-an-environment-variable-on-the-server-that-changes-f

It looks like 128K  (32 \* 4K pages) per string.  So if we can set multiple ENV variables you might be able to pass more data, unless SSH is limiting.

http://man7.org/linux/man-pages/man2/execve.2.html

```
  Limits on size of arguments and environment
       Most UNIX implementations impose some limit on the total size of the
       command-line argument (argv) and environment (envp) strings that may
       be passed to a new program.  POSIX.1 allows an implementation to
       advertise this limit using the ARG_MAX constant (either defined in
       <limits.h> or available at run time using the call
       sysconf(_SC_ARG_MAX)).

       On Linux prior to kernel 2.6.23, the memory used to store the
       environment and argument strings was limited to 32 pages (defined by
       the kernel constant MAX_ARG_PAGES).  On architectures with a 4-kB
       page size, this yields a maximum size of 128 kB.

       On kernel 2.6.23 and later, most architectures support a size limit
       derived from the soft RLIMIT_STACK resource limit (see getrlimit(2))
       that is in force at the time of the execve() call.  (Architectures
       with no memory management unit are excepted: they maintain the limit
       that was in effect before kernel 2.6.23.)  This change allows
       programs to have a much larger argument and/or environment list.  For
       these architectures, the total size is limited to 1/4 of the allowed
       stack size.  (Imposing the 1/4-limit ensures that the new program
       always has some stack space.)  Since Linux 2.6.25, the kernel places
       a floor of 32 pages on this size limit, so that, even when
       RLIMIT_STACK is set very low, applications are guaranteed to have at
       least as much argument and environment space as was provided by Linux
       2.6.23 and earlier.  (This guarantee was not provided in Linux 2.6.23
       and 2.6.24.)  Additionally, the limit per string is 32 pages (the
       kernel constant MAX_ARG_STRLEN), and the maximum number of strings is
       0x7FFFFFFF.
```

#### <img src="https://avatars1.githubusercontent.com/u/76221?v=3" width="50">[Julien Lancien](https://github.com/calexicoz) commented at [2014-09-23 11:55](https://github.com/Russell91/sshrc/issues/18#issuecomment-56508670):

It's ok. It's an acceptable limitation. When I'm sshing to a server I don't need all my config. The essentials is good enough.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 21:25](https://github.com/Russell91/sshrc/issues/18#issuecomment-56592491):

Hexadecimal has 16 symbols / byte => 4 bits/byte => 50% efficiency, so that's not responsible for your problem. I'm guessing that du is misleading you, perhaps due to symbolic links? sshrc will include symbolic link when tarring. Interesting article on 128kb limit though. I've changed the README to reflect the lower recommendation.

#### <img src="https://avatars1.githubusercontent.com/u/76221?v=3" width="50">[Julien Lancien](https://github.com/calexicoz) commented at [2014-09-24 00:34](https://github.com/Russell91/sshrc/issues/18#issuecomment-56610533):

So you were right: `du` was misleading me. My `.vim` is actually 15M. Symbolic links...

I'll work on triming it down.


-------------------------------------------------------------------------------

# [\#17 Issue](https://github.com/Russell91/sshrc/issues/17) `closed`: Can't get it working when ssh'ing to CentOS 5.5/Bash 3.2.25

#### <img src="https://avatars3.githubusercontent.com/u/2539311?v=3" width="50">[r-nicol](https://github.com/r-nicol) opened issue at [2014-09-22 11:32](https://github.com/Russell91/sshrc/issues/17):

The bashsshrc does not seem to run correctly.

I tried running:
bash --rcfile <(echo 'source '$SSHHOME'/.sshrc;')
But no luck.

$SSHHOME does seem to resolve and the following works:

bash --rcfile $SSHHOME/.sshrc
bash --init-file $SSHHOME/.sshrc

The bash on the server is ancient could that be the issue?


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 17:35](https://github.com/Russell91/sshrc/issues/17#issuecomment-56558558):

Hmm, perhaps the <(...) syntax doesn't work for you. Can you try `cat <(echo 3)` ?

#### <img src="https://avatars3.githubusercontent.com/u/2539311?v=3" width="50">[r-nicol](https://github.com/r-nicol) commented at [2014-09-24 08:13](https://github.com/Russell91/sshrc/issues/17#issuecomment-56638227):

That does work and outputs 3.

Interestingly cat <(echo 'source '$SSHHOME'/.sshrc;') outputs the correct expected value. However, it does not seem to like using source, when you do it manually. Dropping source works, as stated in my first comment but putting that in <(echo ...) fails.

I guess the solution is find a replacement for <(echo ...). Thoughts?

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-26 02:11](https://github.com/Russell91/sshrc/issues/17#issuecomment-56911354):

I don't know what to say. If you figure it out let me know.

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-09-29 12:30](https://github.com/Russell91/sshrc/issues/17#issuecomment-57153385):

Could you please reopen it?

I reproduce the issue with a ssh to a centos-5.10 host, with bash 3.2.

It seems bash 3.2 does not support process substitution for --rcfile:

```
$ bash --version
GNU bash, version 3.2.25(1)-release (x86_64-redhat-linux-gnu)
Copyright (C) 2005 Free Software Foundation, Inc.
$ bash --rcfile <(echo "echo test")
$ 
```

On ubuntu 12.04:

```
$ bash --version
GNU bash, version 4.2.25(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2011 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
$ bash --rcfile <(echo "echo test")
test
$ 
```

So the generated file that is finally exec bash --rcfile should have an additional indirection using yet another file to support older bash version. (and supporting redhat 5 is really needed in real life environments).

Maybe just set the content of--rcfile  <(...) directly into $SSHHOME/bashsshrc, and replace "$SSHHOME/bashsshrc" by "bash --rcfile $SSHHOME/bashsshrc" (I'm not sure about additional arguments with "$@" though).

#### <img src="https://avatars3.githubusercontent.com/u/2539311?v=3" width="50">[r-nicol](https://github.com/r-nicol) commented at [2014-09-29 13:05](https://github.com/Russell91/sshrc/issues/17#issuecomment-57157184):

I can't reopen it, I guess only Russell can and I do feel this should be resolved.

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-09-29 13:24](https://github.com/Russell91/sshrc/issues/17#issuecomment-57159529):

After my comment I wrote the patch and proposed it as PR #33, so this issue can now be kept closed.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-29 16:55](https://github.com/Russell91/sshrc/issues/17#issuecomment-57191602):

I'll reopen until I pull in the changes. The patch looks good though.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-10-08 00:52](https://github.com/Russell91/sshrc/issues/17#issuecomment-58288410):

Is this working for everyone now?

#### <img src="https://avatars0.githubusercontent.com/u/263267?v=3" width="50">[Thomas Riccardi](https://github.com/Niluge-KiWi) commented at [2014-10-08 08:51](https://github.com/Russell91/sshrc/issues/17#issuecomment-58328196):

It is for me.

#### <img src="https://avatars3.githubusercontent.com/u/2539311?v=3" width="50">[r-nicol](https://github.com/r-nicol) commented at [2014-10-08 08:52](https://github.com/Russell91/sshrc/issues/17#issuecomment-58328326):

ye seems good. 

shame you removed it from brew tho :(


-------------------------------------------------------------------------------

# [\#16 Issue](https://github.com/Russell91/sshrc/issues/16) `closed`: tmp files are left on server during timeout

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2014-09-22 04:58](https://github.com/Russell91/sshrc/issues/16):

Perhaps there is a way to provide a tty script such that a timeout triggers the final rm command, rather than just dropping the shell and leaving the files on the server. In the meantime, I've ameliorated this problem by changing the default tmp-file to be hidden and moving it to /tmp/.$(whoami).sshrc.XXXX by default so that users can clean out all their tmp files without worrying about clearing another users active sshrc files.


#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 16:17](https://github.com/Russell91/sshrc/issues/16#issuecomment-56398428):

will a bash trap of SIGHUP cleanup the files?

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 16:22](https://github.com/Russell91/sshrc/issues/16#issuecomment-56399057):

Potentially. I looked into this last night but didn't solve.
On Sep 22, 2014 9:17 AM, "Ross Brattain" notifications@github.com wrote:

> will a bash trap of SIGHUP cleanup the files?
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/16#issuecomment-56398428.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 07:12](https://github.com/Russell91/sshrc/issues/16#issuecomment-56483337):

I'm testing a fix that uses:

```
            trap \"rm -rf \$SSHHOME; exit\" 0
```

just before calling $SSHHOME/bashsshrc. I'm still testing but quite hopeful that this will clean up the temp files as soon as the server kills the ssh process.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 17:32](https://github.com/Russell91/sshrc/issues/16#issuecomment-56558189):

This should be fixed in master.


-------------------------------------------------------------------------------

# [\#14 Issue](https://github.com/Russell91/sshrc/issues/14) `closed`: Missing dependencies? "xxd: command not found"

#### <img src="https://avatars3.githubusercontent.com/u/2679665?v=3" width="50">[m4l](https://github.com/m4l) opened issue at [2014-09-22 00:50](https://github.com/Russell91/sshrc/issues/14):

My local machine is Ubuntu 14.4 connecting to a server on Centos 6.5, this is what I see:

sshrc root@server  
root@server's password: 
bash: line 2: xxd: command not found
bash: line 10: xxd: command not found
bash: line 13: xxd: command not found

gzip: stdin: unexpected end of file
tar: Child returned status 1
tar: Error is not recoverable: exiting now
Connection to server closed.

cat ~/.sshrc
echo hi


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 03:26](https://github.com/Russell91/sshrc/issues/14#issuecomment-56325421):

Hmm, this is interesting. Can you verify if xxd is installed on the server by typing `which xxd`?

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 03:34](https://github.com/Russell91/sshrc/issues/14#issuecomment-56325706):

I have a solution for this coded up that checks for missing xxd and exits gracefully with an appropriate warning, but I need to understand a little more about why your server wouldn't have xxd.

#### <img src="https://avatars2.githubusercontent.com/u/853790?v=3" width="50">[Tuomo Tanskanen](https://github.com/tuminoid) commented at [2014-09-22 07:34](https://github.com/Russell91/sshrc/issues/14#issuecomment-56338146):

`xxd` is coming from `vim-common` on Ubuntu, and `vim-common` is not a mandatory package for an Ubuntu installation. It is priority of `important`, which means it is not mandatory part of every Ubuntu system. Same likely applies to CentOS as well, as any editor (even vi(m)) isn't a core package.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 07:36](https://github.com/Russell91/sshrc/issues/14#issuecomment-56338280):

hmm, do you have any idea if there is a similar tool (for hex dumping files) that is more common?

#### <img src="https://avatars0.githubusercontent.com/u/1532071?v=3" width="50">[Evgeni Kolev](https://github.com/edkolev) commented at [2014-09-22 09:00](https://github.com/Russell91/sshrc/issues/14#issuecomment-56346337):

Maybe od or hexdump. Not sure which one is more common.

It may be most portable to use bash's printf to hex dump the files. Here's a quick prototype

``` bash
input_file=/tmp/a

while IFS= read -r -n1 char; do
  printf "%02x" "'$char"
done < "$input_file"
```

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 15:58](https://github.com/Russell91/sshrc/issues/14#issuecomment-56395474):

If you have gnu coreutils can you use base64 to encode with base64.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 20:18](https://github.com/Russell91/sshrc/issues/14#issuecomment-56435878):

anyone else have pros/cons for base64?

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 21:59](https://github.com/Russell91/sshrc/issues/14#issuecomment-56450173):

base64 was added in gnu coreutils v6.0 circa 2006-02-27.

base64 also available via python 2.4+ stdlib oneliner, I haven't look into perl or ruby oneliners.

I don't have OS X to test against, so I don't know if it is present there.

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-22 22:01](https://github.com/Russell91/sshrc/issues/14#issuecomment-56450380):

base64 is in openssl,  http://superuser.com/questions/120796/os-x-base64-encode-via-command-line

#### <img src="https://avatars1.githubusercontent.com/u/1693880?v=3" width="50">[Red5d](https://github.com/Red5d) commented at [2014-09-23 17:06](https://github.com/Russell91/sshrc/issues/14#issuecomment-56554186):

+1 for base64 since it's in coreutils. RedHat server builds also don't include vim-common/xxd, FYI.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 17:13](https://github.com/Russell91/sshrc/issues/14#issuecomment-56555210):

Okay, I'm going to support both xxd OR base64, depending on their
availability. It will take some time though.

On Tue, Sep 23, 2014 at 10:06 AM, Red5d notifications@github.com wrote:

> +1 for base64 since it's in coreutils. RedHat server builds also don't
> include vim-common/xxd, FYI.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/14#issuecomment-56554186.

#### <img src="https://avatars2.githubusercontent.com/u/169181?v=3" width="50">[adam mcgreggor](https://github.com/adamamyl) commented at [2014-09-23 19:45](https://github.com/Russell91/sshrc/issues/14#issuecomment-56578398):

base64 is installed on my 10.9.5 MacOS:

```
adam@aragog:~$ uname -a
Darwin aragog.int.abeyance.org.uk 13.4.0 Darwin Kernel Version 13.4.0: Sun Aug 17 19:50:11 PDT 2014; root:xnu-2422.115.4~1/RELEASE_X86_64 x86_64
```

I don't compile my own kernels on the mac, so assume this is fairly stock.

```
adam@aragog:~$ which base64
/usr/bin/base64
```

so it exists…

```
adam@aragog:~$ file /usr/bin/base64
/usr/bin/base64: Mach-O 64-bit executable x86_64
```

… and is an executable

```
adam@aragog:~$ base64 --help
Version DEBUG
Usage:  base64 [-dhvD] [-b num] [-i in_file] [-o out_file]
  -h, --help     display this message
  -v, --version  display version info
  -d, --debug    enables additional output to stderr
  -D, --decode   decodes input
  -b, --break    break encoded string into num character lines
  -i, --input    input file (default: "-" for stdin)
  -o, --output   output file (default: "-" for stdout)
```

so far, so good.

but now for the really useful part…

```
adam@aragog:~$ base64 --version
Version DEBUG
```

#### <img src="https://avatars1.githubusercontent.com/u/1276487?v=3" width="50">[Ross Brattain](https://github.com/rbbratta) commented at [2014-09-23 19:53](https://github.com/Russell91/sshrc/issues/14#issuecomment-56579498):

Cool, looks like OS X has a different arg for decode, though.   `-D` versus `-d` in coreutils.

#### <img src="https://avatars1.githubusercontent.com/u/1693880?v=3" width="50">[Red5d](https://github.com/Red5d) commented at [2014-09-26 13:00](https://github.com/Russell91/sshrc/issues/14#issuecomment-56957951):

My latest pull request switches it to using base64 and differentiates between "-D" and "-d".

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-10-23 20:37](https://github.com/Russell91/sshrc/issues/14#issuecomment-60305008):

Unfortunately I just couldn't get base64 to work to my satisfaction. The fact that they changed their API between versions is only part of the problem. The version on mac seems to be a DEBUG version or something, and the whole thing seems like it would cause more problems than xxd. I've fixed this by testing for the presence of xxd locally and on the server and giving an explicit error message instead.

#### <img src="https://avatars1.githubusercontent.com/u/1693880?v=3" width="50">[Red5d](https://github.com/Red5d) commented at [2014-10-23 22:06](https://github.com/Russell91/sshrc/issues/14#issuecomment-60317028):

Did you look at my pull request here? https://github.com/Russell91/sshrc/pull/24 Base64 is working fine for me. I've accounted for the different command line options on the different versions.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-10-23 22:20](https://github.com/Russell91/sshrc/issues/14#issuecomment-60318540):

I don't think the -di option works on os x.

Version DEBUG
Usage:  base64 [-dhvD] [-b num] [-i in_file] [-o out_file]
  -h, --help     display this message
  -v, --version  display version info
  -d, --debug    enables additional output to stderr
  -D, --decode   decodes input
  -b, --break    break encoded string into num character lines
  -i, --input    input file (default: "-" for stdin)
  -o, --output   output file (default: "-" for stdout)

On Thu, Oct 23, 2014 at 3:06 PM, Red5d notifications@github.com wrote:

> Did you look at my pull request here? #24
> https://github.com/Russell91/sshrc/pull/24 Base64 is working fine for
> me. I've accounted for the different command line options on the different
> versions.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/14#issuecomment-60317028.

#### <img src="https://avatars1.githubusercontent.com/u/1693880?v=3" width="50">[Red5d](https://github.com/Red5d) commented at [2014-10-24 02:56](https://github.com/Russell91/sshrc/issues/14#issuecomment-60338776):

Yeah, my code checks for that and uses -D instead of -di when needed.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-10-24 03:52](https://github.com/Russell91/sshrc/issues/14#issuecomment-60341785):

Right, but have you tested sshing from a osx machine to a linux machine. It
didn't work for me.

On Thu, Oct 23, 2014 at 7:56 PM, Red5d notifications@github.com wrote:

> Yeah, my code checks for that and uses -D instead of -di when needed.
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/14#issuecomment-60338776.

#### <img src="https://avatars1.githubusercontent.com/u/1693880?v=3" width="50">[Red5d](https://github.com/Red5d) commented at [2014-10-31 16:50](https://github.com/Russell91/sshrc/issues/14#issuecomment-61291092):

Ah, I see. It's only checking for different base64 options on the remote machine, not local. Let me fix that...

#### <img src="https://avatars1.githubusercontent.com/u/1693880?v=3" width="50">[Red5d](https://github.com/Red5d) commented at [2014-11-03 17:07](https://github.com/Russell91/sshrc/issues/14#issuecomment-61511318):

Ok. Try it now. I've pulled in your latest changes and (I think) fixed the base64 options. The pull request has been updated.


-------------------------------------------------------------------------------

# [\#8 Issue](https://github.com/Russell91/sshrc/issues/8) `closed`: Homebrew support

#### <img src="https://avatars1.githubusercontent.com/u/1567498?v=3" width="50">[Johannes Schickling](https://github.com/schickling) opened issue at [2014-09-20 13:26](https://github.com/Russell91/sshrc/issues/8):

Please register this package on homebrew to install it on OSX via `$ brew install sshrc`


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-20 23:04](https://github.com/Russell91/sshrc/issues/8#issuecomment-56283100):

I haven't worked with homebrew before. Maybe you could submit a package and I'll link to it from the readme here?

#### <img src="https://avatars2.githubusercontent.com/u/7490448?v=3" width="50">[Moshe Zada](https://github.com/moshe) commented at [2014-09-21 17:20](https://github.com/Russell91/sshrc/issues/8#issuecomment-56305651):

There is a PR in brew repository that installs sshrc
https://github.com/Homebrew/homebrew/pull/32341
@elmak

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-21 18:25](https://github.com/Russell91/sshrc/issues/8#issuecomment-56307661):

@MosheZada nice, added support to the readme

#### <img src="https://avatars2.githubusercontent.com/u/7490448?v=3" width="50">[Moshe Zada](https://github.com/moshe) commented at [2014-09-21 18:42](https://github.com/Russell91/sshrc/issues/8#issuecomment-56308177):

the PR (pull request) isnt merged with master yet - so OS X cannot install via brew.
please change the readme

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-21 18:55](https://github.com/Russell91/sshrc/issues/8#issuecomment-56308587):

I just successfully installed via homebrew 20 mins ago.
On Sep 21, 2014 11:42 AM, "Moshe Zada" notifications@github.com wrote:

> the PR (pull request) isnt merged with master yet - so OS X cannot install
> via brew.
> please change the readme
> 
> —
> Reply to this email directly or view it on GitHub
> https://github.com/Russell91/sshrc/issues/8#issuecomment-56308177.

#### <img src="https://avatars0.githubusercontent.com/u/1532071?v=3" width="50">[Evgeni Kolev](https://github.com/edkolev) commented at [2014-09-23 18:25](https://github.com/Russell91/sshrc/issues/8#issuecomment-56566354):

The brew version doesn't work for me (sshrc works like regular ssh) but the latest github version works just as expected.


-------------------------------------------------------------------------------

# [\#6 Issue](https://github.com/Russell91/sshrc/issues/6) `closed`: See shellcheck.net

#### <img src="https://avatars2.githubusercontent.com/u/516484?v=3" width="50">[Lukas](https://github.com/superlukas) opened issue at [2014-09-20 09:25](https://github.com/Russell91/sshrc/issues/6):

It found 15 problems.
http://www.shellcheck.net/





-------------------------------------------------------------------------------

# [\#4 Issue](https://github.com/Russell91/sshrc/issues/4) `closed`: This is different from ~/.ssh/rc in what way?

#### <img src="https://avatars2.githubusercontent.com/u/321201?v=3" width="50">[James Sumners](https://github.com/jsumners) opened issue at [2014-09-15 12:47](https://github.com/Russell91/sshrc/issues/4):

SSH already parses an rc file if you create it in `~/.ssh/rc`. So I'm just curious: what problem does this project solve? It should be noted in the README.

http://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch08_04.htm


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-15 18:16](https://github.com/Russell91/sshrc/issues/4#issuecomment-55633290):

The tool sources the ~/.sshrc on your local computer, not your remote computer. This means you can configure a server shared with coworkers when you otherwise couldn't. Also, there is no configuration on the server, which makes keeping track of configurations on multiple servers easier.

I've changed the first sentence in Usage to reflect this.

#### <img src="https://avatars2.githubusercontent.com/u/321201?v=3" width="50">[James Sumners](https://github.com/jsumners) commented at [2014-09-15 22:07](https://github.com/Russell91/sshrc/issues/4#issuecomment-55666680):

I see. Thank you for the clarification.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 21:26](https://github.com/Russell91/sshrc/issues/4#issuecomment-56592583):

Change the readme to more directly state the differences.


-------------------------------------------------------------------------------

# [\#2 Issue](https://github.com/Russell91/sshrc/issues/2) `closed`: aws login messages not displayed with sshrc

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2014-09-12 18:13](https://github.com/Russell91/sshrc/issues/2):

If anyone has any insight into the protocol that is printing this, I'd be interested. I'll look into it myself in the meantime.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-12 18:15](https://github.com/Russell91/sshrc/issues/2#issuecomment-55440738):

Ah, grepping for the welcome message in /etc produced the /etc/motd file.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-21 19:35](https://github.com/Russell91/sshrc/issues/2#issuecomment-56309808):

Can someone more knowledgable explain to me how the /etc/motd system works on ubuntu? I'd like to add support for it so that people feel more comfortable about the similarity between ssh and sshrc. A check for the file followed by a cat of it would be fine, but I'd like to know if non-ubuntu systems have similar systems that would need support as well. Also, is /etc/motd always catted if it exists, etc.?

#### <img src="https://avatars2.githubusercontent.com/u/7490448?v=3" width="50">[Moshe Zada](https://github.com/moshe) commented at [2014-09-21 20:38](https://github.com/Russell91/sshrc/issues/2#issuecomment-56311870):

it occurs because you passing the -t flag that forces tty allocation.
i will check it tomorrow.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 03:35](https://github.com/Russell91/sshrc/issues/2#issuecomment-56325747):

yea this makes sense, I think I will just add a special flag to cat the /etc/motd, but if you can figure out a more general way of doing this that would be great.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-22 03:40](https://github.com/Russell91/sshrc/issues/2#issuecomment-56325949):

Looks like these are configured in /etc/ssh/ssdh_config under PrintMotd and PrintLastLog. It'd be good to parse some sshd_config files and react appropriately where this behavior is nullified by the -t flag.

#### <img src="https://avatars0.githubusercontent.com/u/465527?v=3" width="50">[Jan Larres](https://github.com/majutsushi) commented at [2014-09-22 07:48](https://github.com/Russell91/sshrc/issues/2#issuecomment-56339368):

I think the `-t` option is a red herring, the real issue is that bash is not started as a login shell. Depending on the exact system configuration this will have various consequences, including not printing the motd. If I remember correctly I had a system (I think an old RHEL) which actually checked the executable name of bash and only displayed the motd if it had a `-` in front, which signifies a login shell. So in my own wrapper I had to use this horrible construct in order to make it work properly:

```
exec bash -c "exec -a -bash bash --login -i"
```

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 21:19](https://github.com/Russell91/sshrc/issues/2#issuecomment-56591696):

I've always hated the /etc/motd system in the first place - just a bunch of junk text. But I've added a special case to print it when its available by default for compatibility. It'd be good to automatically read this from the sshd_config settings at some point.

#### <img src="https://avatars0.githubusercontent.com/u/465527?v=3" width="50">[Jan Larres](https://github.com/majutsushi) commented at [2014-09-23 22:56](https://github.com/Russell91/sshrc/issues/2#issuecomment-56602907):

I don't think this is really enough, the shell initialization can do anything it wants differently between login and non-login shells. For example, setting the PATH differently is a common occurrence. So instead of special-casing the motd it would be better to make sure that bash is started as a login shell as I mentioned above.

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-23 23:02](https://github.com/Russell91/sshrc/issues/2#issuecomment-56603410):

The best thing to do is to find a simple variation of `ssh me@myserver -t bash` that actually prints the /etc/motd. Let me know if you find something.

#### <img src="https://avatars1.githubusercontent.com/u/1280103?v=3" width="50">[prilka](https://github.com/prilka) commented at [2016-03-10 12:33](https://github.com/Russell91/sshrc/issues/2#issuecomment-194820414):

majutsushi is absolutely right. This issue is only one result of the non-login shell problem.
On my system i don't have bash-completion with sshrc, because the /etc/profile.d/bash_completion.sh is not executed for a non-login shell.


-------------------------------------------------------------------------------

# [\#1 Issue](https://github.com/Russell91/sshrc/issues/1) `closed`: Tar timestamps warning

#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) opened issue at [2014-09-12 18:09](https://github.com/Russell91/sshrc/issues/1):

It seems that if the local and remote server's clocks are too far apart, tar can throw a warning about future timestamps.


#### <img src="https://avatars2.githubusercontent.com/u/1069617?v=3" width="50">[Russell Stewart](https://github.com/Russell91) commented at [2014-09-12 18:10](https://github.com/Russell91/sshrc/issues/1#issuecomment-55440203):

This is harmless, but the warning has been fixed in master by untarring with the -m command: 
 `-m      (x mode only) Do not extract modification time.  By default, the
                modification time is set to the time stored in the archive.`


-------------------------------------------------------------------------------

