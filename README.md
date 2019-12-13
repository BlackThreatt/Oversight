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
    
To create this neural network model, we used the **Python** programming language and the **Keras** library.

To have a better visibility, we used the **ELK** stack to have a graph that illustrates better the behavior of our network over time.
# Code Setup
The **Python** used in this workshop is version **3.5.2**.

Execute this command to be able to use the following libraries :

    $ pip3 install numpy pandas sklearn keras elasticsearch
    
Versions used in this workshop : 
* Numpy (1.17.4) 
* Pandas (0.24.2)
* Sklearn (0.21.3)
* Keras (2.3.1)
# ELK Setup



# DEMO