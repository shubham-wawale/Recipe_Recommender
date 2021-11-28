FROM node:16
RUN apt-get update
RUN mkdir /home/ubuntu && mkdir /home/ubuntu/project
WORKDIR /home/ubuntu/project
RUN git clone https://github.com/het-patel99/Recipe_Recommender.git
WORKDIR /home/ubuntu/project/Recipe_Recommender/Code/backend/dao/
RUN sed -i 's/##gmail_password##/<INSERT_GMAIL_PWD>/g' mail_param.js
WORKDIR /home/ubuntu/project/Recipe_Recommender/Code/backend
RUN npm install -g n
RUN npm install nodemailer
RUN npm install
CMD ["npx", "nodemon"]