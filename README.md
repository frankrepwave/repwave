# Repwave.ai

## Setup Steps
1. Create an AWS Account: https://aws.amazon.com/getting-started/guides/setup-environment/
2. Install `aws-cli`: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
3. Install Docker: https://docs.docker.com/engine/install/
4. Install AWS Lightsail: https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software
5. Clone this repo

## Build React
1. Run `npm install`

## Build / Test Steps
1. Build Docker container: `docker build -t flask-container .`
2. Test Flask container: `docker run -p 5000:5000 flask-container`
3. Open Browser and go to http://localhost:5000 to see app

## Create a container service Steps
[Don't need to do unless first time setting up]
1. Create container: <br>
`aws lightsail create-container-service --service-name repwave-server --power small --scale 1`
2. See containers being built<br>
`aws lightsail get-container-services`<br>
It will show `"state": "PENDING"`. Look for the state when it's `"state": "READY"`
3. Deploy onto AWS:<br>
`aws lightsail push-container-image --service-name repwave-server --label flask-container --image flask-container`

## Deploy onto AWS
1. Deploy onto AWS:<br>
`aws lightsail push-container-image --service-name repwave-server --label flask-container --image flask-container`
2. Update the `containers.json` file with the correct version number for the container.
3. Run `aws lightsail create-container-service-deployment --service-name repwave-server --containers file://containers.json --public-endpoint file://public-endpoint.json`
4. Run `aws lightsail get-container-services --service-name repwave-server`