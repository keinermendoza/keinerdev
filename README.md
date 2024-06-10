# Hi I'm Keiner

This is keinerdev, My personal site for showecase my work and share
some thougs and learning accros my dev journey.

you can jump streight to the [The Site](https://keinermendoza.com) and see it by your own.

## Why this app is interesting?

I have deploy some servers in the manually way, installing all the dependencies, creating the enviorments pushing the code and configuring some services. So is very frustrating when for any reason i must to change of server.

The must popular solution for that problem is **Docker** and that's great, but...
I cannot develop different apps on the same server with that approach. I like to be able of use **NGINX** for route to different apps in the same server. Dont judge me, I preffer to avoid spend money when I can.

So, this is an implementation of **Django** app in **Docker** network implemented with **docker compose** but with some tweaks:

- NGINX is runing on the docker host routing to different apps
- Static files are deployed an served from Private Oracle Bucket (like S3)
- coninue 