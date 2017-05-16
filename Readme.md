Sample python library not intended for anything other than demonstrating packaging a python program and adding command to the path after installation.
  
  
  install with:
  
  ```bash
  sudo python setup.py install
  ```
  
  To record the files installed use:
  ```bash
  python setup.py install --record files.txt
  ```
  To uninstall you can then use:
  ```bash
  cat files.txt | xargs rm -rf
  ```
  
  