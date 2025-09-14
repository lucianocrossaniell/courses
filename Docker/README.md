https://learn.kodekloud.com/user/courses/docker-training-course-for-the-absolute-beginner/module/672dc9a2-52ce-467f-b00c-c2f16185479b/lesson/8f626b4e-ee33-487c-866a-a0b5c3b07a74

### Basic Docker Commands:

<code> docker run nginx </code> - start the nginx container. If image is not present it will download image

<code>docker ps </code> - list all running contaners and basic info about them

<code>docker stop <container name> </code> - stop container

<code>docker ps -a </code> - see all running containers or not runnings

<code>docker stop $(docker ps -a -q) </code> - stop all containers

<code>docker rm <container name> </code>- removes container permanently

<code>docker rm $(docker ps -a -q) </code> - removes all containers pe

<code>docker images </code> - view list of available images

<code>docker rmi <image name> </code> - removes image, must be sure no containers are being run from that image

<code>docker rmi $(docker images -q) </code> - removes all images on host

<code>docker pull <image name> </code> - pull/download image

<code>docker run <container name> sleep 5 </code>- runs contaner for a duration of 5 seconds

<code>docker exec <container name> cat /etc/host </code>- execute command on docker container

<code>docker run -d <container name> </code>- run docker container in bg mode, container will contiue to run in bg

<code>docker run -d <container name> --name newname </code>- run container with tagged name

<code>docker atache <container id> </code>- attach docker container
