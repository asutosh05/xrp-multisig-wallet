# xrp-multisig-wallet

We will Use Rippled Admin Methods for that we have run our own Rippled Node

Setps to install rippled node (I am following the Ubuntu setup)
https://developers.ripple.com/install-rippled.html

Then we have to edit the config to conncet the test-net
Command to open config file
sudo nano /opt/ripple/etc/rippled.cfg
Then go to IPS section and comment the main-net and uncommnet the test-net

Lets set Alias for rippled

alias rippled="/opt/ripple/bin/rippled --conf=/opt/ripple/etc/rippled.cfg"

Check the status
rippled server_info

Run in standalone mode

Create a copy of systemd unit file

sudo cp /usr/lib/systemd/system/rippled.service /etc/systemd/system/rippled-standalone.service

Edit these lines:

sudo nano /etc/systemd/system/rippled-standalone.service

(Use --load if you have run in network mode and synced already. Use --start for an empty ledger.)

Description=Ripple Daemon Standalone mode

ExecStart=/opt/ripple/bin/rippled --conf /etc/opt/ripple/rippled.cfg -a --load

Then 

sudo systemctl stop rippled
sudo systemctl start rippled-standalone



