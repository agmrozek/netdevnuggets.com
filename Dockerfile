FROM python
RUN pip install flask
COPY ./static /home/ubuntu/static
COPY ./templates /home/ubuntu/templates
COPY ./images /home/ubuntu/images
COPY netdevnuggets.py /home/ubuntu
EXPOSE 8888
CMD python /home/ubuntu/netdevnuggets.py 
