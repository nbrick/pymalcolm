from malcolm.core import method_takes, REQUIRED
from malcolm.core.vmetas import PointGeneratorMeta
from malcolm.controllers.runnablecontroller import RunnableController
from malcolm.parts.ADCore.detectordriverpart import DetectorDriverPart


XSPRESS3_BUFFER = 16384


class Xspress3DriverPart(DetectorDriverPart):
    @RunnableController.Configure
    @method_takes(
        "generator", PointGeneratorMeta("Generator instance"), REQUIRED)
    def configure(self, task, completed_steps, steps_to_do, part_info, params):
        if steps_to_do > XSPRESS3_BUFFER:
            # Set the PointsPerRow from the innermost generator
            gen_num = params.generator.generators[-1].num
            steps_per_row = XSPRESS3_BUFFER // gen_num * gen_num
        else:
            steps_per_row = steps_to_do
        task.put(self.child["pointsPerRow"], steps_per_row)
        super(Xspress3DriverPart, self).configure(
            task, completed_steps, steps_to_do, part_info, params)