docker run --name trainer-env --gpus all --ipc=host --net=host -e DISPLAY=$DISPLAY -v $HOME/.Xauthority:/root/.Xauthority:rw -v "$(pwd)":/workdir --rm -it clayrisee/dataset-utils:1.0.0

# docker run --name trainer-env --gpus all --ipc=host --net=host -e DISPLAY=$DISPLAY -v ("$PWD"):/workdir --rm -it clayrisee/dataset-utils:1.0.0