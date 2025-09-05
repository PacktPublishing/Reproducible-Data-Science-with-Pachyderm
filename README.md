
<b><p align='center'>[![Packt Sale](https://static.packt-cdn.com/assets/images/packt+events/Improve_UX.png)](https://packt.link/algotradingpython)</p></b> 




# Reproducible Data Science with Pachyderm

<a href="https://www.packtpub.com/product/reproducible-data-science-with-pachyderm/9781801074483"><img src="https://static.packt-cdn.com/products/9781801074483/cover/smaller" alt="Data Engineering with AWS" height="256px" align="right"></a>

This is the code repository for [Reproducible Data Science with Pachyderm](https://www.packtpub.com/product/reproducible-data-science-with-pachyderm/9781801074483), published by Packt.

**Learn how to design and build cloud-based data transformation pipelines using AWS**

## What is this book about?

Pachyderm is an open source project that enables data scientists to run reproducible data pipelines and scale them to an enterprise level. This book will teach you how to implement Pachyderm to create collaborative data science workflows and reproduce your ML experiments at scale.

You’ll begin your journey by exploring the importance of data reproducibility and comparing different data science platforms. Next, you’ll explore how Pachyderm fits into the picture and its significance, followed by learning how to install Pachyderm locally on your computer or a cloud platform of your choice. You’ll then discover the architectural components and Pachyderm's main pipeline principles and concepts. The book demonstrates how to use Pachyderm components to create your first data pipeline and advances to cover common operations involving data, such as uploading data to and from Pachyderm to create more complex pipelines. Based on what you've learned, you'll develop an end-to-end ML workflow, before trying out the hyperparameter tuning technique and the different supported Pachyderm language clients. Finally, you’ll learn how to use a SaaS version of Pachyderm with Pachyderm Notebooks.

By the end of this book, you will learn all aspects of running your data pipelines in Pachyderm and manage them on a day-to-day basis.

This book covers the following exciting features: 
* Understand the importance of reproducible data science for enterprise
* Explore the basics of Pachyderm, such as commits and branches
* Upload data to and from Pachyderm
* Implement common pipeline operations in Pachyderm
* Create a real-life example of hyperparameter tuning in Pachyderm
* Combine Pachyderm with Pachyderm language clients in Python and Go

If you feel this book is for you, get your [copy](https://www.amazon.in/Reproducible-Data-Science-Pachyderm-version-controlled/dp/1801074488/ref=sr_1_1?crid=1JRTHXXNKUL2O&keywords=Reproducible+Data+Science+with+Pachyderm&qid=1646808421&sprefix=reproducible+data+science+with+pachyderm%2Caps%2C593&sr=8-1) today!

<a href="https://static.packt-cdn.com/downloads/9781801074483_ColorImages.pdf"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders.

The code will look like the following:
```
image = displacy.render(textfile, style='dep',
options={"compact": True, "distance": 70})
f = open('/pfs/out/pos-tag-dependency.svg', "w")
f.write(image)
f.close()
```
**Following is what you need for this book:**

This book is for new as well as experienced data scientists and machine learning engineers who want to build scalable infrastructures for their data science projects. Basic knowledge of Python programming and Kubernetes will be beneficial. Familiarity with Golang will be helpful.
With the following software and hardware list you can run all code files present in the book (Chapter 1-11).

### Software and Hardware List

| Chapter  | Software required                                                                    | OS required                        |
| -------- | -------------------------------------------------------------------------------------| -----------------------------------|
|  	1-11	   |   	Pachyderm 2.0 |  Windows, Linux Or macOS.|
|  	1-11	   |   	pachctl 2.0 |  Windows, Linux Or macOS.|
|  	1-11	   |   	Helm 3.6|  Windows, Linux Or macOS.|
|  	1-11	   |   	Docker Desktop 2.2.0.5 |  Windows, Linux Or macOS.|
|  	1-11	   |   	minikube1.19 |  Windows, Linux Or macOS.|
|  	1-11	   |   	kubectl v1.18 |  Windows, Linux Or macOS.|
|  	1-11	   |   	eksctl |  Windows, Linux Or macOS.|
|  	1-11	   |   	aws-iam-authenticator 1.21.2 |  Windows, Linux Or macOS.|
|  	1-11	   |   	WSL 2 |  Windows|
|  	1-11	   |   	go1.16.4 drawin/amd64|  Windows, Linux Or macOS.|

We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781800569492_ColorImages.pdf ).

### Related products <Other books you may enjoy>
* Engineering MLOps  [[Packt]](https://www.packtpub.com/product/engineering-mlops/9781800562882) [[Amazon]](https://www.amazon.in/Engineering-MLOps-Rapidly-production-ready-learning/dp/1800562888/ref=sr_1_2_sspa?crid=6J4IU93ITHF&keywords=Engineering+MLOps&qid=1646809140&sprefix=engineering+mlops%2Caps%2C607&sr=8-2-spons&psc=1&smid=A15DBATYR506U3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVkFBU05DOTIyUEtWJmVuY3J5cHRlZElkPUEwNTAxMTE2UUwzTk9FRzhFNTBGJmVuY3J5cHRlZEFkSWQ9QTA1MjM2MzBRSE9EREs0OVhVTVomd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl)
  
* Getting Started with Streamlit for Data Science  [[Packt]](https://www.packtpub.com/product/getting-started-with-streamlit-for-data-science/9781800565500) [[Amazon]](https://www.amazon.in/Getting-Started-Streamlit-Data-Science/dp/180056550X/ref=sr_1_1_sspa?crid=35OVLBEMBZ2RD&keywords=Getting+Started+with+Streamlit+for+Data+Science&qid=1646809150&sprefix=getting+started+with+streamlit+for+data+science%2Caps%2C315&sr=8-1-spons&psc=1&smid=A15DBATYR506U3&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNEcyMzQ2MU9HRVBIJmVuY3J5cHRlZElkPUEwMDI5ODE5MzkwTFVIU0NXS0ZPRCZlbmNyeXB0ZWRBZElkPUEwNTExMDY2MUdIRUxIUlg4V1o0MCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=)
  
## Get to Know the Author
**Svetlana Karslioglu** is a seasoned documentation professional with over 10 years of experience in top Silicon Valley companies. During her tenure at Pachyderm, she authored much of the open source documentation for Pachyderm and was also in charge of the documentation infrastructure. Throughout her career, she has spoken at local conferences and given talks advocating for open infrastructure and unbiased research in artificial intelligence. When Svetlana is not busy writing books, she spends time with her three children and her husband, Murat.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801074483">https://packt.link/free-ebook/9781801074483 </a> </p>