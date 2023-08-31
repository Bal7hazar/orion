mod input_0;
mod input_1;
mod output_0;


use array::ArrayTrait;
use orion::operators::tensor::core::TensorTrait;
use orion::operators::tensor::implementations::tensor_u32_fp16x16::{
    Tensor_i32_fp16x16, u32TensorSub
};
use orion::operators::tensor::implementations::tensor_u32_fp16x16::u32TensorPartialEq;
use orion::utils::assert_eq;

#[test]
#[available_gas(2000000000)]
fn test_sub_u32_broadcast() {
    let input_0 = input_0::input_0();
    let input_1 = input_1::input_1();
    let z = output_0::output_0();

    let y = input_0 - input_1;

    assert_eq(y, z);
}
