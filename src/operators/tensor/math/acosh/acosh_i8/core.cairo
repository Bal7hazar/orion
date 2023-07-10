use orion::numbers::fixed_point::core::{FixedType, FixedImpl};
use orion::operators::tensor::core::{Tensor};
use orion::numbers::signed_integer::i8::i8;
use orion::operators::tensor::math::acosh::acosh_i8::fp8x23;
use orion::operators::tensor::math::acosh::acosh_i8::fp16x16;

/// Cf: TensorTrait::acosh docstring
fn acosh_i8(self: @Tensor<i8>) -> Option<Tensor<FixedType>> {
    match *self.extra {
        Option::Some(extra_params) => match extra_params.fixed_point {
            Option::Some(fixed_point) => match fixed_point {
                FixedImpl::FP8x23(()) => Option::Some(fp8x23::acosh(self)),
                FixedImpl::FP16x16(()) => Option::Some(fp16x16::acosh(self)),
            },
            Option::None(_) => Option::Some(fp16x16::acosh(self)),
        },
        Option::None(_) => Option::Some(fp16x16::acosh(self)),
    }
}
