# report_missing_files

Report missing files that should belong in a sequence.

When copying over large number of files from another device it is good to check that all files did get copied over before deleting the source files.

For example, a mobile device might have 1000 photos but one or two are missing after copying.

Usually (for sure Apple devices) use a sequence number for naming files.

This can be used to detect potentially missing files.

The script will identify all gaps in the sequence numbers and can be used as a sanity check.

Run the script in the directory you are interested in:


```
/YOUR_PATH_TO_THIS_REPO/run.py
```
