# **Work Steps:**

* Open new project in pycharm.

* select python interpreter which installed on my device to:
    `C:\Users\ahmad\AppData\Local\Programs\Python\Python311`

* install pyspark using terminal 
    `pip install pyspark`
    `pip install pyspark[sql]`
* or install spark to your machine as here: `https://sparkbyexamples.com/spark/apache-spark-installation-on-windows/`
 
* install single node Hadoop v3.3.3 as here: `https://brain-mentors.com/hadoopinstallation/`
 
* install jdk8 from the link: `https://www.oracle.com/tr/java/technologies/javase/javase8-archive-downloads.html`
 
* add `JAVA_HOME` and `HADOOP_HOME` to environment variables with the installed path
* add installed path to the path variable too
* if you use spark don't forget to add `SPARK_HOME` variable and path too
 
* put your txt files in the folder `txtFiles`
 
* run and test

# Not:

I tried alot to take files from zip file but, I had a problem after reading zip file and converting it to dataframe
the problem related to python version so, I tried python 2.7, 3.6, 3.9 and 3.11 and the problem still apper so, I skipped
the problem reading files from folder with the wanted conditions.
the problem can be seen in jupyter file.

* **I write another python code to application reading from zip and to match the result in file `pythonCode.py`**