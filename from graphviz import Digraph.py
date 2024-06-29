from graphviz import Digraph

# Create a new Digraph
er_diagram = Digraph('ER Diagram', filename='/mnt/data/er_diagram', format='png')

# Entities
er_diagram.node('Ö', 'Öğrenci\n(ÖğrenciNo, Ad, Soyad, Adres, Derece, GeçmişPerformans)')
er_diagram.node('M', 'Modül\n(ModülKodu, İsim, KrediDeğeri, Bölüm, ModülLideriID, ÖnKoşulModülKodu, ZorunluMu)')
er_diagram.node('ÖG', 'Öğretim Görevlisi\n(ÖğretimGörevlisiID, Ad, Soyad, Bölüm)')

# Relationship Entities
er_diagram.node('MS', 'ModülSeçimi\n(ÖğrenciNo, ModülKodu, SınavSonucu)')
er_diagram.node('MÖ', 'ModülÖğretimi\n(ModülKodu, ÖğretimGörevlisiID)')

# Relationships
er_diagram.edge('Ö', 'MS', label='1, N')
er_diagram.edge('MS', 'M', label='N, 1')
er_diagram.edge('M', 'MÖ', label='1, N')
er_diagram.edge('MÖ', 'ÖG', label='N, 1')

# Self-referencing relationship for prerequisite modules
er_diagram.edge('M', 'M', label='ÖnKoşulModülKodu')

# Render the diagram
er_diagram.view()