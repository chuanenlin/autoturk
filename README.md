# Autoturk

Autoturk is Amazon's Mechanical Turk streamlined for batch sending HIT requests. </br>

## Setting up

1. Sign up for an [AWS account](https://aws.amazon.com/).

2. Sign up for an [MTurk Requester account](https://requester.mturk.com/).

3. [Link your AWS account to your MTurk account](https://requester.mturk.com/developer).

4. *(Optional)* Sign up for a [Sandbox MTurk Requester Account](http://requestersandbox.mturk.com/) to test HIT requests without paying.<br>
Remember to link your Sandbox account to your AWS account as well.

5. [Set up an IAM user for MTurk](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkGettingStartedGuide/SetUp.html#create-iam-user-or-role) and save your access key ID and secret access key strings for later use.

6. Create a bucket on [Amazon S3](https://s3.console.aws.amazon.com/s3/home?region=us-east-1#), upload your photos to the bucket, set your bucket access to public, and save the bucket name string for later use.

7. Open terminal and enter the following lines:
```
cd C:\Python27\Scripts
pip install boto
pip install xmltodict
```

8. Open terminal in the directory where you placed all your photos and enter:
```
dir /b /a-d > image.list (for Windows)
ls > image.list (for Ubuntu)
```

9. Move the generated list from Step 8 to your root directory (where you saved create_hits.py and retrieve_hits.py).

---

## Creating HIT template for Bounding Box

You can use MTurk to assign a large variety of HITs. In this section, I will go through how to set up a HIT template for drawing bounding boxes to label images, based on [Kota's bbox annotator](https://github.com/kyamagu/bbox-annotator).

1. Sign in to your [MTurk Requester account](http://requester.mturk.com/).

2. Click **Create** > **New Project** > **Other** > **Create Project**.

3. Fill in the required fields and click **Design Layout** > **Source**.</br>
I recommend setting *Reward per assignment* to *$0.1*, *Number of assignments per HIT* to *1*, *Time allotted per assignment* to *1*, *HIT expires in* to *7*, *Auto-approve and pay Workers in* to *3*, and *Require that Workers be Masters to do your HITs* to *No*.

4. Paste the code in **src.html** into the editor and adjust the description to your needs.

5. Click **Source** (again) > **Save** > **Preview and Finish** > **Finish**.

6. Click **Create** > **New Batch with an Existing Project** > **[Your project name]** and save the HITType ID and Layout ID strings for later use.

---

## Generating

1. In **generate.py**, change `C:/Users/David/autoturk/image.list` in line 9 to the local path of your list of image filenames.</br>
Change `drone-net` of `https://s3.us-east-2.amazonaws.com/drone-net/` in line 12 to your Amazon S3 bucket name where you've uploaded your images.</br>
Change `[Your_access_key_ID]` in line 14 to your access key ID.</br>
Change `[Your_secret_access_key]` in line 15 to your secret access key.</br>
Change `drone` of `LayoutParameter("objects_to_find", "drone")` in line 19 to your object.</br>
Change `[Your_hit_layout]` in line 22 to your HIT's Layout ID.</br>
Change `[Your_hit_type]` in line 24 to your HIT's HITType ID.</br>

2. *(Optional)* If you are using Sandbox mode, change `mechanicalturk.amazonaws.com` in line 16 to `http://mechanicalturk.sandbox.amazonaws.com`.</br>
Change `https://www.mturk.com/mturk/preview?groupId=` in lines 30 and 31 to `https://workersandbox.mturk.com/mturk/preview?groupId=`.

3. Open terminal in the directory of **generate.py** and enter:
```
python generate.py
```

---

## Retrieving

1. In **retrieve.py**, change `C:/Users/David/autoturk/hit-id.list` in line 16 to the local path of your generated list of HIT IDs.</br>
Change `C:/Users/David/autoturk/image.list` in line 17 to the local path of your list of image filenames.</br>
Change `[Your_access_key_ID]` in line 21 to your access key ID.</br>
Change `[Your_secret_access_key]` in line 22 to your secret access key.</br>
Change `C:/Users/David/autoturk/labels/` in line 34 to the local path of the directory in which you plan to save the annotation txt files for each image.</br>
Change `drone-net` of `https://s3.us-east-2.amazonaws.com/drone-net/` in line 48 to your Amazon S3 bucket name where you've uploaded your images.</br>

2. *(Optional)* If you are using Sandbox mode, change `mechanicalturk.amazonaws.com` in line 23 to `http://mechanicalturk.sandbox.amazonaws.com`.

3. *(Optional)* If you would like to retrieve all annotation txt files at once without visualizing, comment out lines 48 to 61.

4. Open terminal in the directory of **retrieve.py** and enter:
```
python retrieve.py
```

---

## Amazon's Definitions

**Requester**</br>
A Requester is a company, organization, or person that creates and submits tasks (HITs) to Amazon Mechanical Turk for Workers to perform. As a Requester, you can use a software application to interact with Amazon Mechanical Turk to submit tasks, retrieve results, and perform other automated tasks. You can use the Requester website to check the status of your HITs, and manage your account.

**Human Intelligence Task**</br>
A Human Intelligence Task (HIT) is a task that a Requester submits to Amazon Mechanical Turk for Workers to perform. A HIT represents a single, self-contained task, for example, "Identify the car color in the photo." Workers can find HITs listed on the Amazon Mechanical Turk website. For more information, go to the Amazon Mechanical Turk website.</br>
Each HIT has a lifetime, specified by the Requester, that determines how long the HIT is available to Workers. A HIT also has an assignment duration, which is the amount of time a Worker has to complete a HIT after accepting it.

**Worker**</br>
A Worker is a person who performs the tasks specified by a Requester in a HIT. Workers use the Amazon Mechanical Turk website to find and accept assignments, enter values into the question form, and submit the results. The Requester specifies how many Workers can work on a task. Amazon Mechanical Turk guarantees that a Worker can work on each task only one time.

**Assignment**
An assignment specifies how many people can submit completed work for your HIT. When a Worker accepts a HIT, Amazon Mechanical Turk creates an assignment to track the work to completion. The assignment belongs exclusively to the Worker and guarantees that the Worker can submit results and be eligible for a reward until the time the HIT or assignment expires.

**Reward**</br>
A reward is the money you, as a Requester, pay Workers for satisfactory work they do on your HITs.

---

## Updates
