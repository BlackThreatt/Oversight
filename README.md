# Building a Security That Thinks
In this workshop we will present the basics of artificial intelligence as well as an introduction to SIEM (Security Information & Event Management) with an emphasis on its usefulness and  we will present a prototype of an intrusion detection system using artificial intelligence.

Here is our [Presentation](https://drive.google.com/open?id=16bd5i6ss-TRtOmjS7EdxXslJVgeeZfRD).

Realized by: Mohamed Ali BESSAIDI ([BlackThreatt](https://github.com/BlackThreatt)) & Mohamed Hichem ZAYANI ([MHZDeveloper](https://github.com/MHZDeveloper)) & Mohamed OUNIS ([ounismohamed](https://github.com/ounismohamed))

# Description

We have developed an intrusion detection system based on artificial intelligence. The model takes network-based data as input and thus predicts whether it is a normal connection or an attack. If it is an attack, the system also predicts the type of attack.

The input data are composed of :


* duration: continuous
* protocol_type: symbolic
* service: symbolic
* flag: symbolic
* src_bytes: continuous
* dst_bytes: continuous
* land: symbolic
* wrong_fragment: continuous
* urgent: continuous
* hot: continuous
* num_failed_logins: continuous
* logged_in: symbolic
* num_compromised: continuous
* root_shell: continuous
* su_attempted: continuous
* num_root: continuous
* num_file_creations: continuous
* num_shells: continuous
* num_access_files: continuous
* num_outbound_cmds: continuous
* is_host_login: symbolic
* is_guest_login: symbolic
* count: continuous
* srv_count: continuous
* serror_rate: continuous
* srv_serror_rate: continuous
* rerror_rate: continuous
* srv_rerror_rate: continuous
* same_srv_rate: continuous
* diff_srv_rate: continuous
* srv_diff_host_rate: continuous
* dst_host_count: continuous
* dst_host_srv_count: continuous
* dst_host_same_srv_rate: continuous
* dst_host_diff_srv_rate: continuous
* dst_host_same_src_port_rate: continuous
* dst_host_srv_diff_host_rate: continuous
* dst_host_serror_rate: continuous
* dst_host_srv_serror_rate: continuous
* dst_host_rerror_rate: continuous
* dst_host_srv_rerror_rate: continuous

The results that our model can predict :

* back
* buffer_overflow
* ftp_write
* guess_passwd
* imap
* ipsweep
* land
* loadmodule
* multihop
* neptune
* nmap
* normal
* perl
* phf
* pod
* portsweep
* rootkit
* satan
* smurf
* spy
* teardrop
* warezclient
* warezmaster
    
To create this neural network model, we used the **Python** programming language and the **Keras** library on **Linux**.

To have a better visibility, we used the **ELK** stack to have a graph that illustrates better the behavior of our network over time.
# Code Setup
The **Python** used in this workshop is version **3.5.2**.

You need to install the **distutils** and the **setuptools** related to **Python 3** :

    $- sudo apt install python3-distutils python3-setuptools

You need also to install **pip3** :

    $- sudo apt install python3-pip

Execute this command to be able to use the following libraries :

    $ pip3 install numpy pandas scikit-learn tensorflow keras elasticsearch
    
Versions used in this workshop : 
* Numpy (1.17.4) 
* Pandas (0.24.2)
* Sklearn (0.21.3)
* Tensorflow (1.14.0)
* Keras (2.3.1)

In the file **ModelCreation.py**, you'll find how to create a model trained by the [Dataset](https://drive.google.com/open?id=1WEzi6vXPSq9HzrYfg7V0kKFtvKkuoazZ)
20 times.

In the file **Siem.py**, the model will predict the if the network is safe based on users logs.
 
# ELK Setup

Now the ElasticSearch,Logstash and Kibana stack are basically a collection of web applications that needs to communicate information to eachother. To assure that this ecosystem runs in the best conditions there is, we chose to deploy this stack on docker containers . 

#### First Step

So the First step now is to Setup docker in your system . you can skip this step if you already have docker and docker-compose already installed and functionnal :

* First of all we have to update the system , in order to do this , type the following command: 
    
        $- sudo apt update          
    
* Next we install the curl utility, in order to do this , type the following command:  :


        $- sudo apt install apt-transport-https ca-certificates curl software-properties-common
      
* Now we download the docker packages, in order to do this , type the following command:  :

        $- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        
* Next, we add the downloaded repository , in order to do this , type the following command:  :

        $- pip3 install --upgrade requests
        $- sudo add-apt-repository deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable
        
* Now we update the system again so that the changes takes effect :

        $- sudo apt update
       
* Then we add the docker-ce cache policy: 

        $- apt-cache policy docker-ce docker-compose
        
* Finally now , we can run the install command : 

        $- sudo apt install docker-ce docker-compose
        
* Now we check the docker daemon's status, and the docker-compose version : 

        $- sudo systemctl status docker
        $- docker-compose --version 
        
* Now we have to add the current user to the docker users groupe :

        $- sudo usermod -aG docker ${USER}

* Now we have to check that the user is now added to the goupe :

        $- su - ${USER}
 

#### Second Step
            
Now  that we have docker and docker-compose properly installed , we open the terminal and we get to the docker directory in our project :

        $- cd ~/Workspace/Siem/ELK/docker-elk/

#### Third Step
        
Next we build the ELK Stack and start it with the following command (**This step might take somewhile**) :

        $- docker-compose up -d 
            

#### Fourth Step

Now we check the health of our elk stack , to do this we need to type the following command (**We should see 3 running containers , one for Elasticsearch , one for Logstash and the last one for Kibana .**):

        $- docker ps 
             
#### Fifth Step  

Now we can open the Kibana dashbord , in order to do this , go to your internet browser and type the following address (**This should display the Kibana login page , now user the username "elastic" and the password "changeme" to access the dashboard .**):

        http://localhost:5601
         
#### Sixth Step
Once the Kibana interface opens , you should be able to access the dashbords and all the graphics areas .

Next we need to load the dashboard config we make in this prototype , in order to do so, go to the 
**left menu** and scroll down to **the management icon** , then under Kibana section , click on **"Saved Objects"**.

On the top right corner of the interface , click on the **"Import"** Button.

The import widget will open up , then click on import again , you'll be asked to choose a file 
    go to the project directory **(~/Workspace/Siem/ELK/docker-elk/elasticsearch/config/)** and choose **"export.ndjson"**.
    Make sure the **"automatically overwrite all saved objects"** option is **enabled** , and then click on the bottom left blue "Import" Button 

Now that we have the dashboards configured , go ahead and click on the "Dashboard" option in the left menu and choose **"Oversight Dashboard"**, then choose the "This Week" filter and apply it .  

# Execution

Run **Siem.py**.

This will start the simulation of the inbound events flow to our prototype , now every event that comes will have to be evaluated (With the rendered model) , classified (With the created neural network) , indexed (with Elasticsearch) and finally visualized on the dashboard (With Kibana).

# Screenshots


At this level you should be seeing the indexed information appearing in the different graphs , go ahead and play with the parameters as much as you want .. !

Screenshot 1 (not real data)

![Screenshot1](images/1.png?raw=true)

Screenshot 2 (not real data)

![Screenshot2](images/2.png?raw=true)

Screenshot 3 (real data)

![Screenshot3](images/3.png?raw=true)

Screenshot 4 (real data)

![Screenshot4](images/4.png?raw=true)

Screenshot 5 (real data)

![Screenshot5](images/5.png?raw=true) 
