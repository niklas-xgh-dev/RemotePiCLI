# add these lines to your ~/.bashrc

if [ -n "$SSH_CLIENT" ] || [ -n "$SSH_TTY" ]; then
  echo "Welcome to your Raspberry Pi!"
  echo "Type 'rpicli' to start the RPI CLI."
fi

alias rpicli='/usr/local/bin/rpicli'