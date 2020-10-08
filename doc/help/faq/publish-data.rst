Publish data
============

1.  **Should I always share the data of my publication?**

    Yes! Our funding agencies, such as NWO and EU, require this either explicitly in the grant on basis of which you carried out the work, or implicitly in their general regulations. The Radboud University has made open access part of its policy. The Radboud University requires sharing the data.

    There might be reasons why you do not want to share your data immediately, e.g. if you are still working on follow up publications based on the same data. In those cases you should share the data under an embargo of a certain time.

    There might be reasons why you do not want to share your data with everyone, e.g. if it represents financial value. In those cases you should make a custom data use agreement under which the data is to be shared (which might e.g. contain a clause about paying for the data).

    There might be reasons related to the privacy of your subjects and where the data cannot be de-identified. In that case you still might be able to share processed results at the group level that allow other researchers to validate the claims in your paper. Note that unprocessed imaging and MEG/EEG data can be shared after it has been de-identified and under the appropriate `Data Use Agreement <https://data-acc.ru.nl/doc/dua/>`_.

2.  **Can I share my data if they belong to an ongoing project?**

    When a research project is still ongoing (i.e. the Data Acquisition Collection is still open), and the researchers want to write a paper using the data collected until present, then they can create a Data Sharing Collection (DSC) in which the data that were used in the publication are shared. You should document in the DSC that these shared data are part of a larger project, of which only a part is shared in the current DSC.

.. _faq-dsc-files:

3.  **What data should I share in a Data Sharing Collection (DSC)?**

    You should share all data that is of potential value to other researchers: the DSC should contain the relevant information (1) to reproduce the published results, and (2) to extend on these published results.

    However, you should only share data that has been de-identified and that cannot be traced back to the individual. Keep in mind that, in all cases, sharing human data requires that the participants have signed an informed consent form that allows the data to be shared.

    Raw photos, videos or audio files should not be shared in a DSC. (In exceptional cases, sharing is allowed, provided that the participant gave explicit consent for public sharing of this material).

.. _faq-dsc-prepare:

4.  **How should I prepare my datasets before public sharing?**

    Make sure your human subjects data are properly anonymized:
    Anonymization of datasets is required before publication to protect the privacy of research participants. Anonymization must be done according to the guidelines below:

    - Remove all direct identifiers

    - Remove indirect identifiers that are not essential for re-using the data

    - Remove indirect identifiers that have a high 'disclosure risk', e.g., unusual characteristics or a combination of unusual findings (e.g. world leader with      orange skin, or very rare disease and nationality and age)

    - Include as few indirect identifiers as possible

    - Reduce precision of indirect identifiers (e.g., use year of birth or age in years)


    +---------------------------------+--------------------------------------------------+
    | Direct identifiers              | Indirect identifiers (limit, or reduce           |
    | (not allowed)                   | precision)                                       |
    +=================================+==================================================+
    | Name and/or initials            | Gender                                           |
    +---------------------------------+--------------------------------------------------+
    | E-mail address                  | Year of birth                                    |
    +---------------------------------+--------------------------------------------------+
    | Home address                    | Place of birth                                   |
    +---------------------------------+--------------------------------------------------+
    | Telephone number / contact info | Body measures (weight, height)                   |
    +---------------------------------+--------------------------------------------------+
    | Unique ID numbers (BSN, SONA-id)| Socio-economic data (work, income, education)    |
    +---------------------------------+--------------------------------------------------+
    | Video, photo or audio data      | Information about individuals mental / physical  |
    | (voice)                         | well-being                                       |
    +---------------------------------+--------------------------------------------------+
    | Data containing participant's   | Geographic information                           |
    | facial features (MRI: deface)   |                                                  |
    +---------------------------------+--------------------------------------------------+
    | Date of birth                   | Sensitive data (ethnicity, race, sexual          |
    |                                 | orientation and risky behavior)                  |
    +---------------------------------+--------------------------------------------------+
    | Other dates that could be       | Information that may stigmatize a community      |
    | identifying for participant:    | (e.g., membership of religious or political org.)|
    | visit, scan..                   |                                                  |
    +---------------------------------+--------------------------------------------------+
    | Pseudonyms (only allowed if     |                                                  |
    | key-file has been disposed)     |                                                  |
    +---------------------------------+--------------------------------------------------+


5.  **How should I organize the data in the repository (DAC/RDC/DSC)?**

    Organize your collections in a standard way (such as BIDS), because will make it much easier to share the data at a later point in time. Below is one example from the BIDS website. See more examples here.

    .. figure:: images/BIDS.PNG
        :scale: 50%

    For all types of data we recommend that you add a text document (txt, pdf or Microsoft Word) that describes the organization of the data over the files and directories.

.. _faq-files-added-to-DSC:

6.  **Which files are automatically added to my DSC after publication?**

    After publication of the DSC, a MANIFEST, LICENSE and README file are autamatically added to the collection data.

    The MANIFEST file contains a list of all files in the collection with a checksum for each, to check the presence and content of the collection files (see :ref:`here <check-transferred-data>`).

    The LICENSE file contains the selected :ref:` Data Use Agreement <faq-data-use-agreement>`.

    The README file contains relevant collection metadata that is also available from the webportal (i.e., collection title, authors, persistent ID, abstract, background info and restrictions on data access and reuse).


.. _faq-data-use-agreement:

7.  **What is a Data Use Agreement (DUA)?**

    The DUA specifies the conditions under which data in a DSC is shared, e.g. to give attribution. The DUA may also include details on specific limitations on the reuse of the data. As manager or contributor to the DSC you specify under which DUA the data is to be shared. When the external researcher agrees with the collection’s DUA, he/she will be automatically added as a viewer to it, which gives him/her read access.

    The repository supports `several DUAs <https://data-acc.ru.nl/doc/dua/>`_. Please use :dua:`RU-HD-1.0` for collections that include potentially identifiable data from individual human subjects. If a dataset has more specific requirements for data sharing (e.g. due to sensitivity of data or requirements of funders or collaborating partners), it is required to make a custom DUA. For further help, please send an email to datasupport@donders.ru.nl.

    After publication of the DSC, a LICENSE file containing the selected DUA is added to the collection data.

.. _faq-persistent-identifier:

8.  **What is a persistent identifier?**

<<<<<<< HEAD
    A persistent identifier is a long-lasting reference to an online document or file. The Radboud Data Repository persistent identifiers are realized by the handle system. See more on the Wikipedia page: https://en.wikipedia.org/wiki/Persistent_identifier

.. _faq-persistent-identifier-dr:

9.  **Can I use the (reserved) persistent identifier generated by the Radboud Data Repository for my publication?**

    As a prerequisite for publication, several journals now request a persistent identifier of the shared data, which they publish in the footnote of the article. Researchers from the Radboud University can use the persistent identifier of the Data Sharing Collection (DSC) for that purpose.
=======
    A persistent identifier is a long-lasting reference to an online document or file. The Donders Repository persistent identifiers are realized by the DOI system. See more on the Wikipedia page: https://en.wikipedia.org/wiki/Persistent_identifier

.. _faq-persistent-identifier-dr:

9.  **Can I use the DOI generated by the Donders Repository for my publication?**

    As a prerequisite for publication, several journals now request a persistent identifier of the shared data, which they publish in the footnote of the article. Researchers from the Donders Institute can use the digital object identifier (DOI)  of the Data Sharing Collection (DSC) for that purpose.
>>>>>>> 100943e... updates DOI

    .. figure:: images/DOI.png

    Note that a DOI is already assigned as soon as the DSC is created. You can already use it in your manuscript; however, only after *publishing* the DSC, the DOI becomes active and will point to the published DSC. If the editor of the journal requests access to data during the review process - i.e. before publishing the DSC -, use the "reviewer access URL" as described :ref:`here <publish-dsc-share-data>`.

    A published DSC's DOI has the same status as the persistent identifiers that are typically used to refer to published journal articles, also DOIs. A persistent identifier allows for direct access to a digital object, even if its URL has changed.

    When sending the DSC's persistent identifier to the journal, in the email, you should add some additional information pertaining to the conditions under which the shared data can be accessed. Here is a template email that you can use for that purpose:

    - The shared data for paper XXX-YYY can be found via the following persistent identifier: http://doi.org/MyPersistentID (replace this string by the string that you copy and paste from the collection metadata page).

    - If applicable, see :dua:`this page <index>`: Prior to accessing and downloading the shared data, users have to create an account. It is possible to use an institutional account, an ORCID account, or a social ID from Google+, Facebook, Twitter, LinkedIn or Microsoft. After authentication, users must accept the Data Use Agreement (DUA), after which they are automatically authorised to download the shared data. The DUA specifies whether there are any restrictions on how the data may be used.

    - As an example of how to access shared data, one may follow the Digital Object Indentifier (doi) in the data availability segment of the footnote of `this paper <http://dx.doi.org/10.1371/journal.pone.0154881>`_. Instructions for how to request access and to download shared data can be found at :ref:`access-shared-data`.

    - The Radboud University will keep these shared data available for at least 10 years.

10. **Can I share my data without the need for the downloading user to register an account?**

    Yes, but it depends on the type of data you share, and the data use agreement you select, see :dua:`this page <index>`. In general, access to potentially identifiable human data (e.g., MRI data) must be 'restricted' and requires authentication by the user, after which the user has to agree with the specified Data Use Agreement before access is allowed. This is required to protect the privacy of our research participants. Anonymous access to 100% anonymized data is allowed by selecting a general Data Use Agreement or license (that was not specifically designed for RU / DI).

    Journals usually accept that data sets are shared only after registering / access request, if data sets include potentially identifiable human data (e.g. MRI). If the journal questions this, you should explain to the journal why access request, and logging in to the repository, is required to access the data. Here's a template paragraph that you can use for this purpose:

    ::

        All data was acquired in accordance with the declaration of Helsinki, following informed consent of participants and in line with the requirements of the Ethics Committee. In line with requirements of the Ethics Committee and the Radboud University security officer, potentially identifying data (such as imaging data) can only be shared to identifable researchers, hence the requirement for registration and for requesting access. Neither authors nor data steward is involved in granting access to external researchers, this is only based on the complete registration of the researcher and follows a “click-through” procedure. We believe that this procedure is in line with your policy, while at the same time being as open and transparent as possible.

11. **What if a 'published' Data Sharing Collection (DSC) contains incorrect information?**

    If a 'published' DSC contains incorrect and/or insufficient information, a collection manager may ask the research administrator to make it 'editable' again, allowing for changes to be made. If this DSC is modified and thereafter changed to 'published' again, then a second read-only copy is generated, with another unique persistent identifier.

    Since the original collection is persistent, it will remain accessible as well. Therefore, carefully check all the files before changing a DSC to 'published'. See :ref:`publish-dsc-share-data`.

12. **How many publications can be linked to a Data Sharing Collection (DSC)?**

    A DSC can be linked to zero, one or multiple publications. The first situation (no publication) occurs when a data set is considered useful for external researchers in their future studies. The second situation (one publication) typically occurs when a data set is used in a publication, and the DSC is shared around the same time that the paper becomes available on the publisher’s website. The third situation (more publications) typically occurs when a DSC gets reused in other publications following the paper that was published together with DSC.

13. **I just published my DSC by clicking the "switch to published" button; why does my persistent identifier not work?**

    The *actual* publication of a DSC takes time, as a copy of the collection content is created once you click the "switch to published" button on the web portal. Depending on the size of the collection content, it may take a few minutes or hours before your DSC is actually accessible via the persistent identifier.
