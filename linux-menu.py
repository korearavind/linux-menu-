import os
import getpass

os.system("clear")
os.system("tput setaf 3")
print("\t\t--------------------------------")
print("\t\tWELCOME TO THE MENU")
os.system("tput setaf 7")
print("\t\t--------------------------------")


passwd = getpass.getpass("enter the password : ")

if passwd != "andy":
    print("\tpassword is incorrect ....")
    exit()

r = input("where you wnat run commands? local/remote : ")
print(r)

while True:
    print("""
        \n
        press 1: to run common commands
        press 2: to run hadoop
        press 3: to run docker
        press 4: to run lvm partition
	press 0: to exit
        """)

    x = input("enter your choice : ")

    while True:
        if int(x) == 1:
            print("""
                        \n
                        press 1: to check the ip of system                  \tpress 26: to see the data in file 
                        press 2: to run date                                \tpress 27: to add alias to any command
                        press 3: to run cal                                 \tpress 28: to switch to other user
                        press 4: to run firefox                             \tpress 29: to know the process id
                        press 5: to use which command                       \tpress 30: to run tcp dump command
                        press 6: to use gedit                               \tpress 31: to disable the firewall
                        press 7: to change directry                         \tpress 32: to enable the firewall
                        press 8: to know present working direct0ry          \tpress 33: to clear the terminal
                        press 9: to know the list of files in directory     \tpress 34: to know the history of commands on terminal
                        press 10: to ping  to any site/ip                   \tpress 35: to remove a file
                        press 11: to check jobs running                     \tpress 36: to remove  a folder
                        press 12: to bring jobs running back to foreground  \tpress : to exit
                        press 13: to create a directory                     
                        press 14: to kown user on system
                        press 15: to add new user
                        press 16: to run watch commad
                        press 17: to check memory usage in system
                        press 18: to check filesystem 
                        press 19: to print the text entered
                        press 20: to speak the text entered
                        press 21: to know about any command
                        press 22: to know software is there inthe system
                        press 23: to install any software in system using rpm
                        press 24: to run bc(converter binary/decimal/hexa)
                        press 25: to know the ports running 
                        """)

            p = input("Enter the choice : ")
            print(p)

            if r == "local":
                if int(p) == 1:
                    os.system("ifconfig")

                if int(p) == 2:
                    os.system("date")

                elif int(p) == 3:
                    os.system("cal")

                elif int(p) == 4:
                    os.system("firefox")

                elif int(p) == 5:
                    a = input(
                        "enter the command which you want use with 'which' : ")
                    os.system("which {}".format(a))

                elif int(p) == 6:
                    a = input(
                        "enter the command which you want use with 'gedit' : ")
                    os.system("gedit {}".format(a))

                elif int(p) == 7:
                    a = input("enter the name of folder to change dict : ")
                    os.system("cd {}".format(a))

                elif int(p) == 8:
                    os.system("pwd")

                elif int(p) == 9:
                    os.system("ls -lh")

                elif int(p) == 10:
                    a = input("enter the site/ip to ping : ")
                    os.system("ping {}".format(a))

                elif int(p) == 11:
                    os.system("jobs")

                elif int(p) == 12:
                    os.system("fg")

                elif int(p) == 13:
                    a = input("enter the name of dirctory you want create : ")
                    os.system("mkdir {}".format(a))

                elif int(p) == 14:
                    os.system("whoami")

                elif int(p) == 15:
                    a = input("enter the userid you want to add : ")
                    b = input("enter the password you want to add : ")
                    os.system("useradd {}".format(a))
                    os.system("passwd {}".format(a))

                elif int(p) == 16:
                    a = input("enter the name which you want use with watch : ")
                    os.system("watch  {}".format(a))

                elif int(p) == 17:
                    os.system("free -m")

                elif int(p) == 18:
                    os.system("df -h")

                elif int(p) == 19:
                    a = input("enter the text you want to print : ")
                    os.system("echo  {}".format(a))

                elif int(p) == 20:
                    a = input("enter the text to speak : ")
                    os.system("espeak-ng  {}".format(a))

                elif int(p) == 21:
                    a = input("enter the command you want to know : ")
                    os.system("man  {}".format(a))

                elif int(p) == 22:
                    a = input(
                        "enter the software path/name you want to know : ")
                    os.system("rpm -q {}".format(a))

                elif int(p) == 23:
                    a = input(
                        "enter the software path/name you want to install using rpm : ")
                    os.system("rpm -i -v -h {} --force".format(a))

                elif int(p) == 24:
                    os.system("bc")

                elif int(p) == 25:
                    os.system("netstat -tnlp")

                elif int(p) == 26:
                    a = input("enter the file you want to see the data : ")
                    os.system("cat  {}".format(a))

                elif int(p) == 27:
                    a = input("enter the command  you want to add alias : ")
                    os.system("cat  \"{}".format(a))

                elif int(p) == 28:
                    a = input("enter the userid you wnat to switch to : ")
                    os.system("sudo su - {}".format(a))

                elif int(p) == 29:
                    a = input("enter the process name to know the id : ")
                    os.system("pgrep {}".format(a))

                elif int(p) == 30:
                    a = input(
                        "enter the file name/path you want have from tcpdump : ")
                    os.system("tcpdump -i ens3p0 -n -XX -vv > {}".format(a))

                elif int(p) == 31:
                    os.system("systemctl stop firewalld")

                elif int(p) == 32:
                    os.system("systemctl start firewalld")

                elif int(p) == 33:
                    os.system("clear")

                elif int(p) == 34:
                    os.system("history")

                elif int(p) == 35:
                    a = input("enter the file name/path you want to remove : ")
                    os.system("rm -f {}".format(a))

                elif int(p) == 36:
                    a = input(
                        "enter the folder name/path you want to remove : ")
                    os.system("rm -rf {}".format(a))

                elif int(p) == 37:
                    exit()

                else:
                    print("\tnot support")

            elif r == "remote":
                ip = input("enter the ip adress : ")
                print(ip)

                if int(p) == 1:
                    os.system("ssh {} date".format(ip))

                if int(p) == 2:
                    os.system("ssh {} cal".format(ip))

                if int(p) == 3:
                    os.system("ssh {} reboot".format(ip))

                if int(p) == 5:
                    exit()
                else:
                    print("\tnot Support")

            else:
                print("not support login ...")

            input("\n plz enter to cont .....")

        if int(x) == 2:
            print("""
                \n
                press 1: goto hadoop folder
                press 2: Setting Up Hadoop on local system
                press 3: to run Start namenode
                press 4: to run start datenode
                press 5: to run check jps command
                press 6: to run admin  report
                press 7: to run stop datenode 
                press 8: to run Stop namenode
                press 9: to check the file in hadoop
                press 10: to put the file into hadoop
                press 11: to create a file in hadoop using touchz
                press 12: to change the block size of a file
                press 13: to exit
                """)

            p = input("Enter the choice : ")
            print(p)

            if r == "local":
                if int(p) == 1:
                    os.system("cd /etc/hadoop/")

                elif int(p) == 2:
                    print("""
		            Select the option:
		            What you want your system as a : 
		            1: Namenode
		            2: Datanode
                            3: client""")
                    option = int(input("Your choice : "))

                    if option == 1:
                        IP = input("Enter the IP of your System : ")
                        port_no = input("Enter the port no of your choice : ")
                        folder = input(
                            "Enter the the folder you want to create for namenode : ")
                        os.system(
                            "sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
                        print(
                            os.system("sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force"))
                        os.system("mkdir /{}".format(folder))

                        with open("/etc/hadoop/hdfs-site.xml", "w") as out_file:

                            hdfs_line = """<?xml version="1.0"?>
                                        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                        <!-- Put site-specific property overrides in this file. -->

                                        <configuration>

                                        <property>

                                        <name>dfs.name.dir</name>
                                        <value>{}</value>

                                        </property>

                                        </configuration>
                                        """.format(folder)
                        out_file.write(hdfs_line)
                        with open("/etc/hadoop/core-site.xml", "w") as out_file:

                            core_line = """<?xml version="1.0"?>
                                        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                        <!-- Put site-specific property overrides in this file. -->

                                        <configuration>

                                        <property>

                                        <name>fs.default.name</name>
                                        <value>hdfs://{}:{}</value>

                                        </property>

                                        </configuration>
                                        """.format(IP, port_no)
                        out_file.write(core_line)

                        os.system(
                            "sudo hadoop namenode -format {}".format(folder))
                        os.system("sudo hadoop-daemon.sh start namenode")

                    elif option == 2:
                        IP = input("Enter the IP of host/namenode System : ")
                        port_no = input(
                            "Enter the port no. given by hots/namenode choice : ")
                        folder = input(
                            "Enter the the folder you want to create for datanode : ")
                        os.system(
                            "sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
                        print(
                            os.system("sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force"))
                        os.system("mkdir /{}".format(folder))

                        with open("/etc/hadoop/hdfs-site.xml", "w") as out_file:

                            hdfs_line = """<?xml version="1.0"?>
                                        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                        <!-- Put site-specific property overrides in this file. -->

                                        <configuration>

                                        <property>

                                        <name>dfs.data.dir</name>
                                        <value>{}</value>

                                        </property>

                                        </configuration>
                                        """.format(folder)
                        out_file.write(hdfs_line)
                        with open("/etc/hadoop/core-site.xml", "w") as out_file:

                            core_line = """<?xml version="1.0"?>
                                        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                        <!-- Put site-specific property overrides in this file. -->

                                        <configuration>

                                        <property>

                                        <name>fs.default.name</name>
                                        <value>hdfs://{}:{}</value>

                                        </property>

                                        </configuration>
                                        """.format(IP, port_no)
                        out_file.write(core_line)

                        os.system("sudo hadoop-daemon.sh start datanode")

                    elif option == 3:
                        IP = input("Enter the IP of host/namenode System : ")
                        port_no = input(
                            "Enter the port no. given by hots/namenode choice : ")
                        os.system(
                            "sudo rpm -ivh /root/jdk-8u171-linux-x64.rpm")
                        print(
                            os.system("sudo rpm -ivh /root/hadoop-1.2.1-1.x86_64.rpm --force"))

                        with open("/etc/hadoop/core-site.xml", "w") as out_file:

                            core_line = """<?xml version="1.0"?>
                                        <?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

                                        <!-- Put site-specific property overrides in this file. -->

                                        <configuration>

                                        <property>

                                        <name>fs.default.name</name>
                                        <value>hdfs://{}:{}</value>

                                        </property>

                                        </configuration>
                                        """.format(IP, port_no)
                        out_file.write(core_line)

                        os.system("hadoop fs -ls /")

                elif int(p) == 3:
                    os.system("hadoop-deamon.sh start namenode")

                elif int(p) == 6:
                    os.system("hadoop-deamon.sh start datanode")

                elif int(p) == 4:
                    os.system("jps")

                elif int(p) == 5:
                    os.system("hadoop dfsadmin -report")

                elif int(p) == 6:
                    os.system("hadoop-deamon.sh start datanode")

                elif int(p) == 7:
                    os.system("hadoop-deamon.sh stop datanode")

                elif int(p) == 8:
                    os.system("hadoop-deamon.sh stop namenode")

                elif int(p) == 9:
                    os.system("hadoop fs -ls /")

                elif int(p) == 10:
                    a = input(
                        "enter the enter file name/path you want to put in hadoop : ")
                    os.system("hadoop fs -put {} /".format(a))

                elif int(p) == 11:
                    a = input(
                        "enter the file name/path you want to create in hadoop using touchz  : ")
                    os.system("hadoop fs -touchz /{} ".format(a))

                elif int(p) == 12:
                    a = input(
                        "enter the enter the block size you want give  : ")
                    b = input(
                        "enter the enter file name/path you want to put in hadoop : ")
                    os.system("hadoop fs -Ddfs.block.size={} -touchz /{} ".format(a, b))

                elif int(p) == 13:
                    exit()
                else:
                    print("\tnot support")

        elif int(x) == 3:
            print("""
                            1. add docker to configuration file 
                            2: Check running container
                            3: Check available images 
                            4: Launch new container
                            5: to attach a container 
                            6: Stop running conatiner
                            7: all the containers
                            8: remove any image
                            9: Exit from docker menu""")

            a = input("enter your choice : ")

            if int(a) == 1:
                with open("/etc/yum.repos.d/new_docker.repo", "w") as out_file:

                    hdfs_line = """
                                    [docker]
                                    baseurl = https://download.docker.com/linux/centos/7/x86_64/stable/
                                    gpgcheck = 0
                                    name = My docker repo
                """.format(folder)
                out_file.write(hdfs_line)
                os.system("sudo yum install docker-ce --nobest")
            elif int(a) == 2:
                os.system("docker info")
            elif int(a) == 3:
                os.system("docker images ")
            elif int(a) == 4:
                name = input("Enter name you want to give to your os: ")
                print("Select image from following list : ")
                os.system("docker images : ")
                image = input("Enter image name : ")
                version = input("Enter version : ")
                os.system(
                    " docker run -it --name {} {}:{}".format(name, image, version))
            elif int(a) == 5:
                exit()
            elif int(a) == 6:
                os.system("docker  ps -a ")
            elif int(a) == 7:
                print("Select image from following list : ")
                os.system("docker images : ")
                image = input("Enter image name : ")
                version = input("Enter version : ")
                os.system(" docker -rmi -f {}:{}".format(image, version))

            elif int(a) == 8:
                exit()
        elif int(x) == 4:
                print("""
                press 1: Create LVM partition
                press 2: Increase existing LVM partition""")
                
                a = input("enter your choice : ")
                if int(a) == 1:
                    dev = []
                    b = ""
                    print("Creating LVM partition : ")
                    no_device = int(input("Enter no of devices you want to create a LVM : "))
                    for i in range(no_device):	
                        a = "/dev/{}".format(input("Device {}".format(i+1)))
                        b = b + a + " " 
                        dev.append(a)
                    for j in range(len(dev)):
                        os.system("sudo pvcreate {}".format(dev[j]))
                    vg_name = input("Enter your Volume Group Name : ")
                    os.system("sudo vgcreate {} {}".format(vg_name,b))
                    size = input("Enter the size of lvm partition you want : ")
                    lvm_name = input("Enter the name of LVM : ")
                    os.system("sudo lvcreate --size {} --name {} {}".format(size,lvm_name,vg_name))
                    folder=input("Enter the path of folder which is contributing to namenode")
                    os.system("sudo mkfs.ext4 /dev/{}/{}".format(vg_name,lvm_name))	
                    os.system("sudo mount /dev/{}/{} {}".format(vg_name,lvm_name,folder))

                elif int(a) == 2:            
                    size = input("Enter how much space you want to increase : ")
                    vg_name = input("Enter your VG name of LVM")
                    lvm_name = input("Enter your LVM name")
                    os.system("sudo lvextend --size +{} /dev/{}/{}".format(size,vg_name,lvm_name))
                    os.system("sudo resize2fs /dev/{}/{}".format(vg_name,lvm_name))
		
	elif int(x) == 0:
		exit()
