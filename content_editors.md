# Editing the configurable content of the Donders Repository portal

This page explains how to update the configurable contents which is displayed on the Donders Repository portal. This includes the help documentation, but also a lot of the the text that is shown on the portal itself.

This repository serves both for the Radboud Data Repository (RDR) as for the Donders Repository (DR). Each of the instances of the repository has two branches, the _acceptance_ and the _release_.  They serve different purposes in the workflow.

## Workflow

Two roles are involved in the workflow: the _content editor_ which is responsible for updating the contents; and the _content manager_ which brings the update online. Hereafter is the workflow:

1. The _content editor_ modifies contents on the _acceptance_ branch.
1. The _RDR buildserver_ builds the content on the _acceptance_ branch and deploys to _acceptance_ environment (refer to build workflow).
1. The _content editor_ informs the _content manager_ to review the changes by creating a pull request.
     1. The _content manager_ is set as assignee for the pull request
     1. The _contact of the other support team_ is set as reviewer of te pull request.
1. The _contact of the other support team_ indicates with a comment whether they would also like the change.
1. The _content manager_ merges changes from _acceptance_ into the _release_ branch by merging the pull request.
1. The _RDR buildserver_ builds the content on the _release_ branch and deploys to _production_ environment
1. The _content manager_ cherry-picks the commit and adds it the the _acceptance_ branch of the other support team, when the other team agrees.
     1. 1. The _RDR buildserver_ builds the content on the _acceptance_ branch and deploys to _acceptance_ environment

## Build workflow
1. The _RDR buildserver_ check for changes on the repository each 1 minute.
1. In case of success it is deployed to the environment.
1. The outcome of the build is mailed to _content editors_ and _content managers_ selected for that branch.
1. In case of a succesful build the _content editor_ reviews the changes on the acceptance environment.
1. In case of a failed build the _content editor_ tries to resolve the issue themselves or contacts [RDR support](mailto:rdr-support@ru.nl) for support.

The above proces an take 2 minutes in total at max.

## Content management and deployment

Please refer to [this document](content_managers.md) for details.

## How to edit

The configurable contents are organised in GitHub as a git repository, with the following branches:

| Branch         | Role                | Deployed to                    |
| -------------- | ------------------- | -------------------------------|
| rdr-acceptance | Content editor      | https://data-acc.ru.nl         |
| rdr-release    | Content manager     | https://data.ru.nl             |
| dr-acceptance  | Content editor      | https://data-acc.donders.ru.nl |
| dr-release     | Content manager     | https://data.donders.ru.nl     |

Before you start editing make sure you're working on the right branch dependent on your role and the environment you need to deploy to. As a content editor __you should only edit the acceptance branch__.

There are two ways of editing the static content:

### method 1

The first edit method is to modifiy the contents directly on the GitHub web interface. Changes made in this way are committed right way to the repository.

### method 2

The second method is to perform changes on a local copy of the repository. With this method, one could edit contents with a favorite text editor; but knowing a couple of basic Git commands is needed.  Follow the instruction below:

Make a local copy of the repository:

```bash
$ git clone https://github.com/Radboud-University/rdr-configurable-content.git
$ cd rdr-configurable-content
```

Edit the files with your favorite text editor.  With this method, changes need to be committed and pushed to GitHub by

```bash
$ git commit -a -m 'message about the change'
$ git push
```

## What to edit

The configurable content to be modified by the content manager are the following type of data:

- __Indices__ are files providing references or elaborated data for the portal to create human-friendly contents at various places in the portal.
- __Snippets__ are files providing part of the HTML body to be incorporated in various portal pages.
- __Styles__ are files used to provide customised style of the portal.
- __Variables__ are placeholders in certain files that will be replaced by the service code with dynamic values when the configurable content is incorporated in the web page.

### indices

The indices files are directly consumed by the portal code to create content dynamically.  Thus, they are presented in a machine-readable format, such as JSON and CSV, in the repository. Given the flexibility of the JSON format, indices in CSV formats are converted into JSON during the deployment process, using the [tools/csv2json.py](https://github.com/Radboud-University/rdr-configurable-content/blob/master/tools/csv2json.py) script.

A list of indices are given blow:

* [external_urls.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/external_urls.json) contains links to local contents (i.e. contents provides by this repository) or remote resources (i.e internet resources).  The local contents are specified with `/` followed by a path relative to the repository's directory; while the remote resources are specified with a URI protocol, such as `http://` or `https://`.

* [doc/dua/data_use_agreement.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/dua/data_use_agreement.json) provides a list of Data Use Agreements, each has its `id`, `name`, and relative `path` to the content.  Note that the `path` is provided as a relative path as the content are provided locally from the repository.  This list is used by the portal to generate the DUA options on the collection editing form of the Data-Sharing Collections.  The order is respected.

* [doc/ethics/ethics_review_board.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/ethics/ethics_review_board.json) provides a list of Ethical Review Boards, and they are grouped in different categories.  This list is used by the portal to generate the Ethical Review Board options on the collection editing form of the Data-Acquisition Collections.  The order is also respected.

* [doc/publication/publication_systems.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/publication/publication_systems.json) provids a list of supported resource identifier systems that are used by the portal to generate the Publication System options on the collection editing form of the Data-Sharing Collections.  Each item on the list shoudl consists of the full name (`system`), the short name (`pidType`), and the URL prefix (`urlPrefix`).

* [doc/keyword/MeSH2015.csv](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/keyword/MeSH2015.csv) and [doc/keyword/SFN2013.csv](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/keyword/SFN2013.csv) are two controlled vocabularies currently supported by the Radboud Data Repository for collection keywords.  They are provided in the CSV format, and will be converted to a JSON format during the deployment.  __For the moment, adding a new keyword set requires development works in the Radboud Data Repository.__

As the JSON documents are imported by the portal code, invalid JSON document can cause errors.  Therefore, all the JSON indices come with a schema file for validating the JSON document during the build process. This process prevents broken JSON indices being deployed to the production system. __One should make sure the schema matches the modified JSON file so that the build process will not fail.__  

### snippets

Snippets are HTML files that will be inserted in relevant portal pages, providing useful information to the portal users.  For a consistent look-n-feel on the portal, one should prevent any CSS-styling in the snippet.

Supported snippets are listed below:

* [doc/login.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/login.html) contains text to be shown on the portal's login page, after the user clicks on the `LOG IN` button.

* [doc/logout.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/logout.html) contains text to be shown on the portal after the user logs out the portal.

* [doc/signup.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/signup.html) contains text to be shown on the portal after the user signed up to the portal the first time.

* [doc/homepage.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/homepage.html) contains text to be shown on the portal's homepage.

* [doc/footer.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/footer.html) contains text to be shown on the footer of every portal page.

* [doc/privacy_policy.html](https://github.com/Radboud-University/rdr-configurable-content/blob/dr-release/doc/privacy_policy.html) contains the privacy policy of the Radboud Data Repository.

* [doc/requestaccess.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/requestaccess.html) contains text guiding user to request data access to a published collection.  The text is used, e.g., in the "Content" tab of the collection detail page.

* [doc/downloadcontent.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/downloadcontent.html) contains text guiding user to download data via a data access method, such as WebDAV.

* [doc/email/collectionChangesLeadText.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/email/collectionChangesLeadText.html) provides leading message of the notification email concerning recent collection changes.

* [doc/email/managerLessCollectionsLeadText.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/email/managerLessCollectionsLeadText.html) provides leading message of the notification email concerning manager-less collections.

* [doc/collection/publish/files_reserved.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/files_reserved.html) contains text informing user the collection could not be published because it has reserved files.

* [doc/collection/publish/publishing.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/publishing.html) contains text informing user the collection is being published.

* [doc/collection/publish/readme.txt](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/readme.txt) contains the readme file to be added to a collection when published.

* [doc/dua/\*.html](https://github.com/Radboud-University/rdr-configurable-content/blob/dr-acceptance/doc/dua/RU-DI-HD-1.0.html) provides contents of a specific data use agreement.

### styles

Currently, the CSS-style is coded in the portal code.  The only customisable components in style are logo and background.

* [doc/style/logo.png](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/style/logo.png): A 100px height logo in png format (logo.png). Width can vary but the height is important to keep the aspect ratio.

* [doc/style/logo@2x.png](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/style/logo@2x.png): A 200px height logo in png format for retina screens. Width can vary but the height is important to keep the aspect ratio.

### variables
To make the configurable content more dynamic a number of variables is supported that are replaced by the system with actual values. For instance, the footer text is configurable and displays the software version. The syntax for using variables is as follows: `${variable name}`. For example: `${version}`.
The following variables are supported, which is a combination of variables that can be used everywhere (without context) and ones that are only available within a certain context:

| Variable | Description | Context |
| -------- | ------- | ----------- |
|`version`| Software version ||
|`year`| Current year ||
|`repositoryDescription`| The repository description. Either Radboud Data Repository for RDR or Donders Repository for DR ||
|`repositoryUrl`| The portal URL. Either https://data.ru.nl for RDR or https://data.donders.ru.nl for DR ||
|`repositoryWebdavUrl`| The WebDAV URL. Either https://webdav.data.ru.nl for RDR or https://webdav.data.donders.ru.nl for DR ||
|`repositoryWebdavPublicUrl`| The public WebDAV URL. Either https://public.data.ru.nl for RDR or https://public.data.donders.ru.nl for DR ||
|`repositorySupportEmail`| The email address to use to get support. Either rdmsupport@ubn.ru.nl for RDR or datasupport@donders.ru.nl for DR ||
|`repositoryHostname`| The repository hostname, useful when one of the more specific URLs above does not suffice. Either data.ru.nl for RDR or data.donders.ru.nl for DR ||
|`userCount`| Number of users (excluding system accounts) ||
|`collectionDscPublishedCount`| Number of Data Sharing Collections that have been published ||
|`collectionDscDraftCount`| Number of Data Sharing Collections that have not been published ||
|`collectionDacArchivedCount`| Number of Data Acquisition Collections that have been archived ||
|`collectionDacDraftCount`| Number of Data Acquisition Collections that have not been archived ||
|`collectionRdcArchivedCount`| Number of Research Documentation Collections that have been archived ||
|`collectionRdcDraftCount`| Number of Research Documentation Collections that have not been archived ||
|`collectionSizeTotal`| Total size of all collections in the repository ||
|`collectionSizeInBytesTotal`| Total size of all collections in the repository in bytes ||
|`downloadLink`| Link to download the Collection's content ||[doc/downloadcontent.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/downloadcontent.html)|
|`collectionAbstract`| The collection's abstract |[doc/collection/publish/readme.txt](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/readme.txt)|
|`collectionPersistentIdentifier`|Persistent identifier link to access the collection's metadata |[doc/collection/publish/readme.txt](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/readme.txt)|
|`collectionTitle`| The collection's title |[doc/collection/publish/readme.txt](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/readme.txt)
|`collectionPublicationYear`| The year in which the collection has been published |[doc/collection/publish/readme.txt](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/readme.txt)|
|`readmeFile`| Name of the readme file which is created when a collection is published |[doc/collection/publish/reserved_files.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/files_reserved.html)|
|`licenseFile`| Name of the license file that contains the data use agreement which is created when a collection is published |[doc/collection/publish/files_reserved.html](https://github.com/Radboud-University/rdr-configurable-content/blob/master/doc/collection/publish/files_reserved.html)|

Please be aware that when using variables that do not exist within a certain context the system will not be able to present the corresponding page on the web portal, or send out corresponding emails.

## Online helps

By making use of the index file [external_urls.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/external_urls.json), the portal provides a mechanism allowing content manager to link various help buttons in the portal to subject-specific help documents that are hosted externally to the portal. It is achieved by adding a key-value pair in the [external_urls.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/external_urls.json) with the identifier of the help button as the key, and the link to the help documentation as the value.

### find online help identifiers

The way to find the help-button identifiers is to login to the web portal, and follow the steps below:

1. Goto an page in which you want to add the online helps
1. On the browser's navigation bar, add `&help` to the URL, and reload the page
1. On the reloaded page, hover the mouse on the question marks. The identifier should be shown in the label. The identifier is a dot(`.`)-separated string.  When the link of the online help has already been provided, the question mark will be "activated"; otherwise, it is gray-outed.

### Adding online helps

Once you have found the identifier, modify the two files: 

1. [external_urls.json](https://github.com/Radboud-University/rdr-configurable-content/blob/master/external_urls.json) to specify the URL of the online help identifier.
1. [external_urls.schema](https://github.com/Radboud-University/rdr-configurable-content/blob/master/external_urls.schema) to accept the new attribute for the JSON validation.
