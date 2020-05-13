.. _publish-dsc-share-data:

Publish DSC and share data
==========================

To share your research data with researchers other than your collaborators you can use a :ref:`Data Sharing Collection <faq-collection-types>` (DSC) (see this FAQ: :ref:`Which files should and should I not upload to a DSC? <faq-dsc-files>`.

A DSC should be published together with the publication of the manuscript. Similar to the publication process in scientific journals, the DSC can follow an internal and external review process before being published.

.. note::

    Please note that only the manager of a collection can publish a collection.

By publishing a DSC, your research data are made publicly available. If you do not want to share your data immediately (e.g. if you are still working on follow up publications based on the same data), you should share the data under an embargo period of a certain time. In the embargo period the published DSC is visible on the web portal with a subset of the collection details. However, the access to its data content will not be publicly available. The embargo period can only be set by the research administrator. Therefore, when requesting a DSC :ref:`(see this FAQ) <faq-how-to-request-collection>` make sure you specify the embargo period.

When publishing the DSC, you also need to select your "data use agreement" :ref:`(see this FAQ) <faq-data-use-agreement>`

To publish a DSC, you must initially follow the same internal review procedure as described for archiving a :ref:`Data Acquisition Collection (DAC) or a Research Documentation Collection (RDC)<archive-dac-rdc>`.

.. note::

    Note that a (reserved) :ref:`persistent identifier <faq-persistent-identifier-DR>` is assigned to a DSC immediately after the colleciton is created. If required, you can already add this persistent identifier to your manuscript; however, only after *publishing* the collection, the persistent identifier becomes active and will point to the published DSC.

If all collaborators agree on the content of the collection, you may want or be requested to allow external reviewers to access your DSC before publishing it.

When the status of the current DSC is "reviewable internal", you can change its status to "reviewable external" by clicking the button and confirming the state change. In this state, the collection is still read-only.

.. figure:: images/switch_to_reviewable_external.jpg

A collection-specific URL is available specifically for external reviewers to access your collection. This URL should only be shared with the editor of the journal to which you send your manuscript. You can retrieve the URL by clicking the "get reviewer access URL" button. Any reviewer that uses the link is added to the DSC having the same rights a viewer has.

.. figure:: images/get_reviewer_access_url.jpg

When sharing the URL with the journal editor, make sure to include a small explanation about how to access the repository and download data. Here's a template e-mail that you can use for that:

::

    The reviewable data for paper XXX-YYY can be found via the following URL: https://data-acc.ru.nl/login/reviewer-CollectionSpecificURL (replace CollectionSpecificURL by the string that you copy and paste when clicking the "get reviewer access" button). The URL provided should only be shared with reviewers. The data will only be publicly available after manuscript acceptance, in which case the persistent identifier that is currently reserved for this collection will become effective.

By following the URL, reviewers can view the data sharing collection in their web-browser and can download the collection content according to the instructions found at :ref:`access shared data <access-shared-data>`.

After external review, the DSC may require changes. This can be done by making the DSC editable again (click button "switch to editable"). The internal and external review process for the data publication can be repeated if required.

When the manuscript is accepted for publication, the Data Sharing Collection should be published by changing its state from "reviewable external" to "published" by clicking the "switch to published" button.

.. figure:: images/switch_to_published.jpg

.. note::

    Keep in mind that this step is irreversible! See below for information about re-opening a published collection. Note that the *actual* publication process takes some time (e.g., several minutes or hours), depending on the size of the data collection.


.. figure:: images/collection_being_published.png

After the collection is published a permanent read-only copy of the collection will be created and the :ref:`persistent identifier <faq-persistent-identifier-DR>` that was assigned will become active. The persistent identifier can be used for future references.

A few details of a DSC can still be changed - using the "edit metadata" button - after it has been published, e.g., linking publications to it, and changing its collection users.

After the collection is published, a version number (1) is assigned. In addition, a MANIFEST, LICENSE and README file are added to the collection data (see :ref:`this faq <faq-files-added-to-DSC>`).

.. figure:: images/metadata_published_collection.jpg

In case you discover mistakes in your collection content, it is possible to re-open a collection. However, be aware that it is not preferred, as creating a second version of the collection will use double the amount of storage space.

.. note::

    As indicated when clicking the "switch to editable" button, you must contact `datasupport@donders.ru.nl <datasupport@donders.ru.nl>`_ to reopen the collection.

After the collection has been reopened, an "editable" *draft version* is created. You can edit the collection content in the same way as before publishing it. You can still view the details of "Version 1", but these are no longer editable and you cannot edit its content.

.. figure:: images/reopend_dsc_draft.jpg

Once you have updated the *draft* version of your collection, you should follow the same procedure for publishing the collection again, as described before on this page.

After publishing this collection, a new version number (2) is assigned.
