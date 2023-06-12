use orion::numbers::fixed_point::core::{FixedType, FixedImpl};
use orion::operators::tensor::core::{Tensor};
use orion::operators::tensor::math::greater::greater_fp::fp8x23;
use orion::operators::tensor::math::greater::greater_fp::fp16x16;

/// Cf: TensorTrait::greater docstring
fn greater(y: @Tensor<FixedType>, z: @Tensor<FixedType>) -> Option<Tensor<usize>> {
    match *y.extra {
        Option::Some(extra_params) => match extra_params.fixed_point {
            Option::Some(fixed_point) => match fixed_point {
                FixedImpl::FP8x23(()) => Option::Some(fp8x23::greater(y, z)),
                FixedImpl::FP16x16(()) => Option::Some(fp16x16::greater(y, z)),
            },
            Option::None(_) => Option::Some(fp16x16::greater(y, z)),
        },
        Option::None(_) => Option::Some(fp16x16::greater(y, z)),
    }
}