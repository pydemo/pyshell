FROM node:12.18.1
RUN mkdir -p /home/alexb/app/node_modules && chown -R node:node /home/alexb/app

WORKDIR /home/alexb/app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install

COPY --chown=node:node . .

CMD [ "node" ]
