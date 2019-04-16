from main import EHooke
from cells import CellManager

app = EHooke()
app.load_base_image("test_phase.tiff")
app.compute_mask()
app.load_fluor_image("test_fluor.tiff")
app.load_option_image("test_fluor.tiff")
app.compute_segments()
app.parameters.cellprocessingparams.find_septum = True
app.cell_manager = CellManager(app.parameters)
app.cell_manager.compute_cells(app.parameters.cellprocessingparams,
                               app.image_manager,
                               app.segments_manager)
app.cell_manager.process_cells(app.parameters.cellprocessingparams,
                               app.image_manager)

print(len(app.cell_manager.cells))