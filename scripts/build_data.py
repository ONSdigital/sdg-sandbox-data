from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
  if data_footnote in meta:
    footnote = meta['data_footnote']
    meta['data_footnote']="<br><ol><li>"+data_footnote.replace(";","</li><li>")+"</li></ol>"
  
  return meta
    
    

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
