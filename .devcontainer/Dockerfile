FROM quay.io/jupyter/base-notebook

USER root
# Generally, Dev Container Features assume that the non-root user (in this case jovyan)
# is in a group with the same name (in this case jovyan). So we must first make that so.
ENV NB_GID=1000
ENV GRANT_SUDO=yes

RUN groupadd jovyan \
    && usermod -g jovyan -a -G sudo jovyan