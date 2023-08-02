import numpy as np
from nodegen.node import RunAll
from ..helpers import make_node, make_test, to_fp, Tensor, Dtype, FixedImpl


class Greater(RunAll):
    @staticmethod
    def greater_u32():
        def default():
            x = np.random.randint(0, 6, (3, 3, 3)).astype(np.uint32)
            y = np.random.randint(0, 6, (3, 3, 3)).astype(np.uint32)
            z = np.greater(x, y)

            x = Tensor(Dtype.U32, x.shape, x.flatten())
            y = Tensor(Dtype.U32, y.shape, y.flatten())
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_u32"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        def broadcast():
            x = np.random.randint(0, 6, (3, 3, 3)).astype(np.uint32)
            y = np.random.randint(0, 6, (1, 3, 1)).astype(np.uint32)
            z = np.greater(x, y)

            x = Tensor(Dtype.U32, x.shape, x.flatten())
            y = Tensor(Dtype.U32, y.shape, y.flatten())
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_u32_broadcast"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        default()
        broadcast()

    @staticmethod
    def greater_i32():
        def default():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.int32)
            y = np.random.randint(-3, 3, (3, 3, 3)).astype(np.int32)
            z = np.greater(x, y)

            x = Tensor(Dtype.I32, x.shape, x.flatten())
            y = Tensor(Dtype.I32, y.shape, y.flatten())
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_i32"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        def broadcast():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.int32)
            y = np.random.randint(-3, 3, (1, 3, 1)).astype(np.int32)
            z = np.greater(x, y)

            x = Tensor(Dtype.I32, x.shape, x.flatten())
            y = Tensor(Dtype.I32, y.shape, y.flatten())
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_i32_broadcast"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        default()
        broadcast()

    @staticmethod
    def greater_i8():
        def default():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.int8)
            y = np.random.randint(-3, 3, (3, 3, 3)).astype(np.int8)
            z = np.greater(x, y)

            x = Tensor(Dtype.I8, x.shape, x.flatten())
            y = Tensor(Dtype.I8, y.shape, y.flatten())
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_i8"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        def broadcast():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.int8)
            y = np.random.randint(-3, 3, (1, 3, 1)).astype(np.int8)
            z = np.greater(x, y)

            x = Tensor(Dtype.I8, x.shape, x.flatten())
            y = Tensor(Dtype.I8, y.shape, y.flatten())
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_i8_broadcast"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        default()
        broadcast()

    @staticmethod
    def greater_fp8x23():
        def default():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.float64)
            y = np.random.randint(-3, 3, (3, 3, 3)).astype(np.float64)
            z = np.greater(x, y)

            x = Tensor(Dtype.FP8x23, x.shape, to_fp(
                x.flatten(), FixedImpl.FP8x23), FixedImpl.FP8x23)
            y = Tensor(Dtype.FP8x23, y.shape,  to_fp(
                y.flatten(), FixedImpl.FP8x23), FixedImpl.FP8x23)
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_fp8x23"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        def broadcast():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.float64)
            y = np.random.randint(-3, 3, (1, 3, 1)).astype(np.float64)
            z = np.greater(x, y)

            x = Tensor(Dtype.FP8x23, x.shape, to_fp(
                x.flatten(), FixedImpl.FP8x23), FixedImpl.FP8x23)
            y = Tensor(Dtype.FP8x23, y.shape,  to_fp(
                y.flatten(), FixedImpl.FP8x23), FixedImpl.FP8x23)
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_fp8x23_broadcast"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        default()
        broadcast()

    @staticmethod
    def greater_fp16x16():
        def default():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.float64)
            y = np.random.randint(-3, 3, (3, 3, 3)).astype(np.float64)
            z = np.greater(x, y)

            x = Tensor(Dtype.FP16x16, x.shape, to_fp(
                x.flatten(), FixedImpl.FP16x16), FixedImpl.FP16x16)
            y = Tensor(Dtype.FP16x16, y.shape,  to_fp(
                y.flatten(), FixedImpl.FP16x16), FixedImpl.FP16x16)
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_fp16x16"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        def broadcast():
            x = np.random.randint(-3, 3, (3, 3, 3)).astype(np.float64)
            y = np.random.randint(-3, 3, (1, 3, 1)).astype(np.float64)
            z = np.greater(x, y)

            x = Tensor(Dtype.FP16x16, x.shape, to_fp(
                x.flatten(), FixedImpl.FP16x16), FixedImpl.FP16x16)
            y = Tensor(Dtype.FP16x16, y.shape,  to_fp(
                y.flatten(), FixedImpl.FP16x16), FixedImpl.FP16x16)
            z = Tensor(Dtype.U32, z.shape, z.flatten())

            name = "greater_fp16x16_broadcast"
            make_node([x, y], [z], name)
            make_test([x, y], z, "input_0.greater(@input_1)", name)

        default()
        broadcast()
