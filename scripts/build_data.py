from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
  if data_footnote in meta:
    footnote = meta['data_footnote']
    footnote_parts=
    new_footnote="<br><ol style='padding-left: 9rem;'><li>"+data_footnote.replace(";","</li><li>")+"</li></ol>"
    

open_sdg_build(config='config_data.yml')
