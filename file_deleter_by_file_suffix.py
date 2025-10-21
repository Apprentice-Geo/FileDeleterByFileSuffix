import os
import sys
from pathlib import Path
class FileDelBySuf:
    def __init__(self):
        self.suffixs=None
        self.dryRun=True

    def setSuffixs(self,suffixs):
        if isinstance(suffixs, str):
            self.suffixs = {suffixs.lstrip('.')}
        else:
            self.suffixs = set(s.lstrip('.') for s in suffixs)

    def setDryRun(self,dryRun):
        self.dryRun=dryRun
    
    @staticmethod
    def getSuffix(fileName,join_multi=True):
        name=Path(fileName).name
        suffixes=[x.lstrip('.') for x in Path(name).suffixes]
        if len(suffixes)>0:
            return ".".join(suffixes) if join_multi else suffixes[-1]
        return None
    
    def deleter(self,path):
        if self.getSuffix(path) not in self.suffixs:
            return
        if self.dryRun:
            print(f"[Dry Run] Deleted {path}")
            return
        try:
            os.remove(path)
            print(f"Deleted {path}")
        except Exception as e:
            print(f"Failed to delete {path}:{e}")
            
    def fileTraversal(self,path):
        if os.path.isfile(path):
            self.deleter(path)
            return
        if not os.path.isdir(path):
            print(f"Not found: {path}")
            return
        for root,dirs,files in os.walk(path):
            for file in files:
                fullPath=os.path.join(root,file)
                self.deleter(fullPath)
