# Managing and deploying the configurable content of the Donders Repository portal

This page explains how to update the configurable contents which is displayed on the Donders Repository portal.

This repository has two branches, the _master_ and the _release_.  They serve different purposes in the following workflow from editing the contents to managing how these changes appear online.

## The workflow

Two roles are involved in the workflow: the _content editor_ which is responsible for updating the contents; and the _content manager_ which brings the update online.  Hereafter is the workflow:

1. The _content editor_ modifies contents on the _master_ branch.
1. The _content editor_ informs the _content manager_ to apply changes to the Donders Repository portal.
1. The _content manager_ merges changes in the _master_ branch into the _release_ branch.  Whenever changes are made in the _release_ branch, an automatic process will pick them up and apply them on the portal.
1. The _content manager_ receives a notification from the automatic process about the result of the process.

## Content editing

Please refer to [this document](content_editors.md) for details.

## Verify the updated content

1. download the repository

  ```bash
  $ git clone https://github.com/Radboud-University/rdr-configurable-content
  ```

2. create distribution zip file

  ```bash
  $ cd rdm-configurable-content-donders
  $ make -f Makefile dist
  ```

  This makefile target will do the following things in a sequential order:

  - convert CSV files into JSON documents (e.g. the controlled vocabularies of keywords)
  - validate JSON documents as long as the corresponding `.schema` file is presented
  - create the release package (`rdm-configurable-content-*.tar.gz`) taking into account only the needed files (e.g. derived HTML snippets and JSON documents) for deployment
  - walk through the `external_urls.json` file in the release zip, check whether the URLs are (or will be) available after the deployment

## Deploy the updated content

The deployment process is triggered by changes in the `release` branch of the repository. After the changes in the `master` branch is confirmed, one can update the `release` branch using the following git commands:

```bash
$ git checkout release
$ git rebase master
$ git push
```
