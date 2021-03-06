from django.db import models

class speciesRecords(models.Model):
    scientificName = models.CharField(max_length=255, null=True, blank=True)
    conservationIUCNGlobal = models.CharField(max_length=255, null=True, blank=True)
    conservationIUCNEurope = models.CharField(max_length=255, null=True, blank=True)
    conservationRedBookPt = models.CharField(max_length=255, null=True, blank=True)
    conservationN2000 = models.CharField(max_length=255, null=True, blank=True)
    conservationN2000Code = models.CharField(max_length=255, null=True, blank=True)
    mainMediaFile = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    descriptionSource = models.TextField(null=True, blank=True)

    class Meta:
      verbose_name_plural = "species"

    def __str__(self):
        return str(self.scientificName)

class biodiversityRecords(models.Model):
    modified = models.CharField(max_length=10, null=True, blank=True)
    license = models.TextField(null=True, blank=True)
    rightsHolder = models.CharField(max_length=255, null=True, blank=True)
    accessRights = models.CharField(max_length=255, null=True, blank=True)
    bibliographicCitation = models.TextField(null=True, blank=True)
    datasetName = models.CharField(max_length=255, null=True, blank=True)
    basisOfRecord = models.CharField(max_length=255, null=True, blank=True)
    dataGeneralizations = models.CharField(max_length=255, null=True, blank=True)
    occurrenceID = models.IntegerField(null=True, blank=True)
    recordNumber = models.IntegerField(null=True, blank=True)
    recordedBy = models.CharField(max_length=255, null=True, blank=True)
    individualCount = models.FloatField(null=True, blank=True)
    organismQuantity = models.FloatField(null=True, blank=True)
    organismQuantityType = models.CharField(max_length=255, null=True, blank=True)
    sex = models.CharField(max_length=255, null=True, blank=True)
    lifeStage = models.CharField(max_length=255, null=True, blank=True)
    reproductiveCondition = models.CharField(max_length=255, null=True, blank=True)
    behavior = models.CharField(max_length=255, null=True, blank=True)
    establishmentMeans = models.CharField(max_length=255, null=True, blank=True)
    occurrenceStatus = models.CharField(max_length=255, null=True, blank=True)
    associatedMedia = models.CharField(max_length=255, null=True, blank=True)
    associatedReferences = models.CharField(max_length=255, null=True, blank=True)
    associatedSequences = models.CharField(max_length=255, null=True, blank=True)
    occurrenceRemarks = models.CharField(max_length=255, null=True, blank=True)
    materialSample = models.CharField(max_length=255, null=True, blank=True)
    materialSampleID = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)
    samplingProtocol = models.CharField(max_length=255, null=True, blank=True)
    sampleSizeValue = models.FloatField(null=True, blank=True)
    sampleSizeUnit = models.CharField(max_length=255, null=True, blank=True)
    samplingEffort = models.CharField(max_length=255, null=True, blank=True)
    fieldNotes = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    locality = models.CharField(max_length=255, null=True, blank=True)
    minimumDepthInMeters = models.FloatField(null=True, blank=True)
    maximumDepthInMeters = models.FloatField(null=True, blank=True)
    verbatimDepth = models.FloatField(null=True, blank=True)
    decimalLatitude = models.FloatField(null=True, blank=True)
    decimalLongitude = models.FloatField(null=True, blank=True)
    geodeticDatum = models.CharField(max_length=255, null=True, blank=True)
    coordinateUncertaintyInMeters = models.FloatField(null=True, blank=True)
    georeferenceProtocol = models.CharField(max_length=255, null=True, blank=True)
    georeferenceRemarks = models.TextField(null=True, blank=True)
    identifiedBy = models.CharField(max_length=255, null=True, blank=True)
    dateIdentified = models.CharField(max_length=255, null=True, blank=True)
    identificationVerificationStatus = models.CharField(max_length=255, null=True, blank=True)
    identificationRemarks = models.TextField(null=True, blank=True)
    scientificNameID = models.CharField(max_length=255, null=True, blank=True)
    acceptedNameUsageID = models.CharField(max_length=255, null=True, blank=True)
    parentNameUsageID = models.CharField(max_length=255, null=True, blank=True)
    scientificName = models.CharField(max_length=255, null=True, blank=True)
    acceptedNameUsage = models.CharField(max_length=255, null=True, blank=True)
    parentNameUsage = models.CharField(max_length=255, null=True, blank=True)
    nameAccordingTo = models.CharField(max_length=255, null=True, blank=True)
    namePublishedIn = models.CharField(max_length=255, null=True, blank=True)
    namePublishedInYear = models.IntegerField(null=True, blank=True)
    Kingdom = models.CharField(max_length=255, null=True, blank=True)
    Phylum = models.CharField(max_length=255, null=True, blank=True)
    Class = models.CharField(max_length=255, null=True, blank=True)
    Order = models.CharField(max_length=255, null=True, blank=True)
    Family = models.CharField(max_length=255, null=True, blank=True)
    Genus = models.CharField(max_length=255, null=True, blank=True)
    taxonRank = models.CharField(max_length=255, null=True, blank=True)
    scientificNameAuthorship = models.CharField(max_length=255, null=True, blank=True)
    taxonomicStatus = models.CharField(max_length=255, null=True, blank=True)
    taxonRemarks = models.TextField(null=True, blank=True)
    measurementType = models.CharField(max_length=255, null=True, blank=True)
    measurementValue = models.FloatField(null=True, blank=True)
    measurementAccuracy = models.CharField(max_length=255, null=True, blank=True)
    measurementUnit = models.CharField(max_length=255, null=True, blank=True)
    measurementMethod = models.CharField(max_length=255, null=True, blank=True)
    measurementRemarks = models.TextField(null=True, blank=True)
    SampleType = models.CharField(max_length=255, null=True, blank=True)
    SampleDesign = models.CharField(max_length=255, null=True, blank=True)
    SampleN = models.FloatField(null=True, blank=True)
    SampleCollector = models.CharField(max_length=255, null=True, blank=True)
    SampleStorageLabel = models.CharField(max_length=255, null=True, blank=True)
    SampleStorageLocation = models.CharField(max_length=255, null=True, blank=True)
    SampleConservationMethod = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
      verbose_name_plural = "records"

    def __str__(self):
        return str(self.scientificName)
