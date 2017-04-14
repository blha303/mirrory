#!/usr/bin/env python3

import yaml
import requests
import sys

def get_sites():
    with open("sites.yaml") as f:
        return yaml.load(f)

def pomf_upload(files):
    req_f = [("files[]", f) for f in files]
    outp = []
    for site in get_sites()["pomf"]:
        if " " in site:
            site, endpoint = site.split(" ", 1)
        else:
            endpoint = site
        d = requests.post("https://{}/upload.php".format(site), files=req_f).json()
        if not d["success"]:
            print("Failed to upload to " + site, file=sys.stderr)
            outp[site] = False
            continue
        outp.append(" ".join(f["url"] if "://" in f["url"] else "https://{}/{}".format(endpoint, f["url"]) for f in d["files"]))
        print("Uploaded to " + site, file=sys.stderr)
    return outp

def main():
    from argparse import ArgumentParser
    import os.path
    parser = ArgumentParser(prog="mirrory")
    parser.add_argument("files", nargs="+", help="Files to upload")
    args = parser.parse_args()
    files = []
    for file in args.files:
        with open(file, "rb") as f:
            files.append((os.path.basename(file), f.read()))
    urls = []
    if "pomf" in get_sites():
        urls += pomf_upload(files)

    print("\n".join(urls))
    return 0

if __name__ == "__main__":
    sys.exit(main())
