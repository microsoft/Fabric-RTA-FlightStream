## Pipeline Artifacts

### Geospatial Sample dataset
* _50_ (grand-parent) invokes > _pipeline_ (parent) invokes > _load_ (child). 
  * Pipelines do not support having foreach within foreach. 
  * The first 2 have foreach loops for iterations and parrallel batches. 
  * This method allows downloading historical once into the lakehouse and ingest ~2B rows/hr, +24M rows/minute to hit +20TBs loaded in just a few hours. 
  * If copy activities fail due to aka.ms/adflimits and you require to ingest many batches in a short period of time for higher throughput then these can be executed from PaaS (Synapse Pipelines / ADF). 
  * ie. more worksapces, additional parrallel/simultanious batches can ingest to KQL DB - going beyond fabric wks limits. 

### Strings - dialog dataset
* _Transcript_ is stream simulation of dialog between pilots & tower, _TranscriptRandom_ is like a historical load but using 1 of 3 relative url(s) of Lorem Ipsums at random.
* Warning: not included above, but be aware that guids as strings provide very uneffective parquet compression.


### Note
* This repo doesnt not provide sample data. Running the pipelines will help you get the sample data from public HTTP linked services.
